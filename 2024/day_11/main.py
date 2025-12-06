import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from collections import Counter

def solve(lines, blinks):
    # Parse initial stones
    initial_stones = list(map(int, lines[0].strip().split()))
    stone_counts = Counter(initial_stones)

    for _ in range(blinks):
        new_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                mid = len(s) // 2
                left = int(s[:mid])
                right = int(s[mid:])
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts

    return sum(stone_counts.values())

def part_one(lines):
    return solve(lines, 25)

def part_two(lines):
    return solve(lines, 75)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))

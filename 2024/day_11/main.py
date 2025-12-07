import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from functools import cache

def blink_stone(stone):
    """Apply the transformation rules to a single stone."""
    if stone == 0:
        return [1]

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        # Split into two stones
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]

    return [stone * 2024]

def simulate_blinks(stones, num_blinks):
    """Simulate blinking for a given number of times (brute force)."""
    current = stones[:]
    for _ in range(num_blinks):
        next_stones = []
        for stone in current:
            next_stones.extend(blink_stone(stone))
        current = next_stones
    return len(current)

@cache
def count_stones_after_blinks(stone, blinks_remaining):
    """Count stones produced by a single stone after a given number of blinks.
    Uses memoization for efficiency."""
    if blinks_remaining == 0:
        return 1

    if stone == 0:
        return count_stones_after_blinks(1, blinks_remaining - 1)

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return (count_stones_after_blinks(left, blinks_remaining - 1) +
                count_stones_after_blinks(right, blinks_remaining - 1))

    return count_stones_after_blinks(stone * 2024, blinks_remaining - 1)

def part_one(lines):
    stones = list(map(int, lines[0].split()))
    return simulate_blinks(stones, 25)

def part_two(lines):
    stones = list(map(int, lines[0].split()))
    total = sum(count_stones_after_blinks(stone, 75) for stone in stones)
    return total

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

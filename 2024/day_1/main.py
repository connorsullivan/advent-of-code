import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from collections import Counter

def part_one(lines):
    left_list = []
    right_list = []
    for line in lines:
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))

    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

def part_two(lines):
    left_list = []
    right_list = []
    for line in lines:
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))

    right_counts = Counter(right_list)

    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts[num]

    return similarity_score

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))

import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    # Parse the two lists from the input
    left_list = []
    right_list = []

    for line in lines:
        if line.strip():  # Skip empty lines
            parts = line.split()
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance

def part_two(lines):
    # Parse the two lists from the input
    left_list = []
    right_list = []

    for line in lines:
        if line.strip():  # Skip empty lines
            parts = line.split()
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))

    # Count occurrences in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        count_in_right = right_counts.get(num, 0)
        similarity_score += num * count_in_right

    return similarity_score

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

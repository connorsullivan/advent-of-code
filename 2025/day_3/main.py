import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def get_max_joltage(s, k):
    rem = len(s) - k
    stack = []
    for char in s:
        while rem > 0 and stack and char > stack[-1]:
            stack.pop()
            rem -= 1
        stack.append(char)
    return int("".join(stack[:k]))

def part_one(lines):
    total = 0
    for line in lines:
        if line.strip():
            total += get_max_joltage(line.strip(), 2)
    return total

def part_two(lines):
    total = 0
    for line in lines:
        if line.strip():
            total += get_max_joltage(line.strip(), 12)
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

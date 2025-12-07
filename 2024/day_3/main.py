import sys
import os
import re

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Find all valid mul(X,Y) instructions and sum their products."""
    # Join all lines into one string
    memory = ''.join(lines)

    # Pattern to match mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.findall(pattern, memory)

    total = 0
    for x, y in matches:
        total += int(x) * int(y)

    return total

def part_two(lines):
    """Handle do() and don't() instructions to enable/disable mul operations."""
    # Join all lines into one string
    memory = ''.join(lines)

    # Pattern to match mul(X,Y), do(), or don't()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

    matches = re.finditer(pattern, memory)

    enabled = True  # mul instructions start enabled
    total = 0

    for match in matches:
        instruction = match.group(0)

        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul") and enabled:
            # Extract the numbers from the mul instruction
            x, y = match.group(1), match.group(2)
            total += int(x) * int(y)

    return total

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

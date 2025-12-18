import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    position = 50
    zeros = 0
    for line in lines:
        if not line:
            continue
        direction = line[0]
        steps = int(line[1:])
        if direction == "L":
            position = (position - steps) % 100
        else:
            position = (position + steps) % 100
        if position == 0:
            zeros += 1
    return zeros

def part_two(lines):
    position = 50
    zeros = 0
    for line in lines:
        if not line:
            continue
        direction = line[0]
        steps = int(line[1:])
        if direction == "R":
            first_hit = (100 - position) % 100 or 100
        else:
            first_hit = position or 100
        if steps >= first_hit:
            zeros += 1 + (steps - first_hit) // 100
        position = (position + steps) % 100 if direction == "R" else (position - steps) % 100
    return zeros

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

import sys
import os
import re

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input, read_input_raw

def part_one(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    return total

def part_two(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, data)

    enabled = True
    total = 0

    for x, y, do_instr, dont_instr in matches:
        if do_instr:
            enabled = True
        elif dont_instr:
            enabled = False
        else:
            # It's a mul instruction
            if enabled:
                total += int(x) * int(y)

    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    data = read_input_raw(input_path)

    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

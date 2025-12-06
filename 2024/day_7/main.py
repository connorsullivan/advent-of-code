import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def check_equation(target, numbers, use_concat):
    def backtrack(index, current_val):
        if index == len(numbers):
            return current_val == target

        if current_val > target:
            return False

        next_num = numbers[index]

        # Try +
        if backtrack(index + 1, current_val + next_num):
            return True

        # Try *
        if backtrack(index + 1, current_val * next_num):
            return True

        # Try ||
        if use_concat:
            concatenated = int(str(current_val) + str(next_num))
            if backtrack(index + 1, concatenated):
                return True

        return False

    return backtrack(1, numbers[0])

def parse_line(line):
    parts = line.split(':')
    target = int(parts[0])
    numbers = list(map(int, parts[1].strip().split()))
    return target, numbers

def part_one(lines):
    total = 0
    for line in lines:
        target, numbers = parse_line(line)
        if check_equation(target, numbers, use_concat=False):
            total += target
    return total

def part_two(lines):
    total = 0
    for line in lines:
        target, numbers = parse_line(line)
        if check_equation(target, numbers, use_concat=True):
            total += target
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))

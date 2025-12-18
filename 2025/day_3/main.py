import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    total = 0
    for line in lines:
        digits = [int(ch) for ch in line.strip()]
        if len(digits) < 2:
            continue
        suffix_max = [0] * len(digits)
        current = -1
        for i in range(len(digits) - 1, -1, -1):
            current = max(current, digits[i])
            suffix_max[i] = current
        best = 0
        for i in range(len(digits) - 1):
            best = max(best, digits[i] * 10 + suffix_max[i + 1])
        total += best
    return total

def part_two(lines):
    k = 12
    total = 0
    for line in lines:
        digits = [int(ch) for ch in line.strip()]
        target = min(k, len(digits))
        stack = []
        for idx, d in enumerate(digits):
            remaining = len(digits) - idx
            while stack and len(stack) + remaining - 1 >= target and stack[-1] < d:
                stack.pop()
            if len(stack) < target:
                stack.append(d)
        number = int("".join(str(d) for d in stack))
        total += number
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

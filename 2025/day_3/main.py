import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _max_subsequence_number(digits: str, k: int) -> int:
    digits = digits.strip()
    if k <= 0:
        return 0
    if k >= len(digits):
        return int(digits) if digits else 0

    to_remove = len(digits) - k
    stack: list[str] = []
    for ch in digits:
        while to_remove and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)
    if to_remove:
        stack = stack[:-to_remove]
    return int("".join(stack[:k]))


def part_one(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        digits = [ord(c) - 48 for c in line]
        suffix_max = [0] * (len(digits) + 1)
        for i in range(len(digits) - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], digits[i])
        best = 0
        for i in range(len(digits) - 1):
            best = max(best, digits[i] * 10 + suffix_max[i + 1])
        total += best
    return total

def part_two(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        total += _max_subsequence_number(line, 12)
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

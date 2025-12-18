import sys
import os
from math import prod

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input_raw

def _split_problems(raw_lines: list[str]) -> list[list[str]]:
    if not raw_lines:
        return []
    width = max(len(line) for line in raw_lines)
    rows = [line.rstrip("\n").ljust(width) for line in raw_lines]
    height = len(rows)

    separators = [all(rows[r][c] == " " for r in range(height)) for c in range(width)]
    blocks: list[tuple[int, int]] = []
    c = 0
    while c < width:
        while c < width and separators[c]:
            c += 1
        if c >= width:
            break
        start = c
        while c < width and not separators[c]:
            c += 1
        end = c
        blocks.append((start, end))

    problems: list[list[str]] = []
    for start, end in blocks:
        problems.append([row[start:end] for row in rows])
    return problems


def _operator(block: list[str]) -> str:
    op_row = block[-1]
    if "+" in op_row:
        return "+"
    if "*" in op_row:
        return "*"
    raise ValueError(f"Missing operator in block: {op_row!r}")


def part_one(lines):
    problems = _split_problems(lines)
    total = 0
    for block in problems:
        op = _operator(block)
        nums: list[int] = []
        for row in block[:-1]:
            digits = "".join(ch for ch in row if ch.isdigit())
            if digits:
                nums.append(int(digits))
        if op == "+":
            total += sum(nums)
        else:
            total += prod(nums) if nums else 0
    return total

def part_two(lines):
    problems = _split_problems(lines)
    total = 0
    for block in problems:
        op = _operator(block)
        body = block[:-1]
        if not body:
            continue
        w = len(body[0])
        nums: list[int] = []
        for col in range(w - 1, -1, -1):
            digits: list[str] = []
            for row in body:
                ch = row[col]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                nums.append(int("".join(digits)))
        if op == "+":
            total += sum(nums)
        else:
            total += prod(nums) if nums else 0
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    raw = read_input_raw(input_path)
    lines = raw.splitlines()
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

import sys
import os
from functools import reduce
import operator

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input_raw

def parse_blocks(raw_lines):
    max_len = max(len(line) for line in raw_lines)
    padded = [line.ljust(max_len) for line in raw_lines]
    rows = len(padded)
    cols = max_len
    separators = [all(padded[r][c] == " " for r in range(rows)) for c in range(cols)]
    blocks = []
    c = 0
    while c < cols:
        if separators[c]:
            c += 1
            continue
        start = c
        while c < cols and not separators[c]:
            c += 1
        blocks.append((start, c))
    return blocks, padded

def extract_operator(op_block):
    for ch in op_block:
        if ch.strip():
            return ch
    return "+"

def part_one(lines):
    blocks, padded = parse_blocks(lines)
    number_rows = padded[:-1]
    op_row = padded[-1]
    total = 0
    for start, end in blocks:
        nums = []
        for row in number_rows:
            chunk = row[start:end].strip()
            if chunk:
                nums.append(int(chunk))
        op = extract_operator(op_row[start:end])
        if op == "+":
            total += sum(nums)
        else:
            total += reduce(operator.mul, nums, 1)
    return total

def part_two(lines):
    blocks, padded = parse_blocks(lines)
    number_rows = padded[:-1]
    op_row = padded[-1]
    total = 0
    for start, end in blocks:
        width = end - start
        op = extract_operator(op_row[start:end])
        nums = []
        for col in range(width - 1, -1, -1):
            digits = []
            for row in number_rows:
                ch = row[start + col]
                if ch != " ":
                    digits.append(ch)
            if digits:
                nums.append(int("".join(digits)))
        if op == "+":
            total += sum(nums)
        else:
            total += reduce(operator.mul, nums, 1)
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    raw = read_input_raw(input_path).splitlines()
    print(f"Part One: {part_one(raw)}")
    print(f"Part Two: {part_two(raw)}")

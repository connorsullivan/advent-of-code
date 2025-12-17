import sys
import os
from functools import reduce
import operator

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def get_blocks(lines):
    if not lines:
        return []

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    num_cols = max_len
    blocks = []
    current_block_start = None

    for c in range(num_cols):
        is_space_col = all(padded_lines[r][c] == ' ' for r in range(len(padded_lines)))

        if not is_space_col:
            if current_block_start is None:
                current_block_start = c
        else:
            if current_block_start is not None:
                blocks.append((current_block_start, c - 1))
                current_block_start = None

    if current_block_start is not None:
        blocks.append((current_block_start, num_cols - 1))

    return blocks, padded_lines

def part_one(lines):
    blocks, padded_lines = get_blocks(lines)
    total = 0

    for start, end in blocks:
        # Last row is the operator
        op_char = padded_lines[-1][start:end+1].strip()
        if not op_char:
            # Try to find the operator in the last row of the block
            for c in range(start, end + 1):
                if padded_lines[-1][c] in '+*':
                    op_char = padded_lines[-1][c]
                    break

        if op_char == '+':
            op = operator.add
        elif op_char == '*':
            op = operator.mul
        else:
            continue

        numbers = []
        for r in range(len(padded_lines) - 1):
            num_str = padded_lines[r][start:end+1].strip()
            if num_str:
                numbers.append(int(num_str))

        if numbers:
            total += reduce(op, numbers)

    return total

def part_two(lines):
    blocks, padded_lines = get_blocks(lines)
    total = 0

    for start, end in blocks:
        # Last row is the operator
        op_char = padded_lines[-1][start:end+1].strip()
        if not op_char:
            for c in range(start, end + 1):
                if padded_lines[-1][c] in '+*':
                    op_char = padded_lines[-1][c]
                    break

        if op_char == '+':
            op = operator.add
        elif op_char == '*':
            op = operator.mul
        else:
            continue

        numbers = []
        # Read columns from right to left
        for c in range(end, start - 1, -1):
            num_str = "".join(padded_lines[r][c] for r in range(len(padded_lines) - 1)).strip()
            if num_str:
                numbers.append(int(num_str))

        if numbers:
            total += reduce(op, numbers)

    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    # We need to read the input exactly as it is, including leading spaces
    with open(input_path, 'r') as f:
        lines = f.readlines()
    # Remove trailing newlines but keep leading/trailing spaces on the line
    lines = [line.rstrip('\n\r') for line in lines]

    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

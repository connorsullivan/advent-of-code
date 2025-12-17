import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    blank_idx = -1
    for i, line in enumerate(lines):
        if not line:
            blank_idx = i
            break

    if blank_idx == -1:
        range_lines = [l for l in lines if '-' in l]
        id_lines = [l for l in lines if '-' not in l and l]
    else:
        range_lines = lines[:blank_idx]
        id_lines = lines[blank_idx+1:]

    ranges = []
    for line in range_lines:
        if '-' in line:
            try:
                start, end = map(int, line.split('-'))
                ranges.append((start, end))
            except ValueError:
                continue

    available_ids = []
    for line in id_lines:
        if line:
            try:
                available_ids.append(int(line))
            except ValueError:
                continue

    return ranges, available_ids

def part_one(lines):
    ranges, available_ids = parse_input(lines)
    count = 0
    for aid in available_ids:
        for start, end in ranges:
            if start <= aid <= end:
                count += 1
                break
    return count

def part_two(lines):
    ranges, _ = parse_input(lines)
    if not ranges:
        return 0

    ranges.sort()

    merged = []
    curr_start, curr_end = ranges[0]
    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
    merged.append((curr_start, curr_end))

    total = 0
    for start, end in merged:
        total += (end - start + 1)
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

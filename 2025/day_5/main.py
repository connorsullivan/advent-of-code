import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse(lines):
    split_idx = lines.index("")
    ranges = []
    for i in range(split_idx):
        start, end = lines[i].split("-")
        ranges.append((int(start), int(end)))
    ids = [int(x) for x in lines[split_idx + 1:]]
    ranges.sort()
    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1] + 1:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return [(s, e) for s, e in merged], ids

def in_ranges(value, merged):
    import bisect
    starts = [s for s, _ in merged]
    idx = bisect.bisect_right(starts, value)
    if idx == 0:
        return False
    s, e = merged[idx - 1]
    return s <= value <= e

def part_one(lines):
    merged, ids = parse(lines)
    return sum(1 for value in ids if in_ranges(value, merged))

def part_two(lines):
    merged, _ = parse(lines)
    return sum(e - s + 1 for s, e in merged)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_ranges(lines):
    parts = [p for p in lines[0].split(",") if p]
    ranges = []
    for part in parts:
        start, end = part.split("-")
        ranges.append((int(start), int(end)))
    ranges.sort()
    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1] + 1:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return [(s, e) for s, e in merged]

def in_ranges(value, merged):
    import bisect
    starts = [s for s, _ in merged]
    idx = bisect.bisect_right(starts, value)
    if idx == 0:
        return False
    s, e = merged[idx - 1]
    return s <= value <= e

def part_one(lines):
    merged = parse_ranges(lines)
    max_end = merged[-1][1]
    min_start = merged[0][0]
    max_len = len(str(max_end))
    candidates = set()
    for total_len in range(2, max_len + 1, 2):
        half = total_len // 2
        start = 10 ** (half - 1)
        end = 10 ** half
        for pat in range(start, end):
            num = int(str(pat) * 2)
            if num > max_end:
                break
            candidates.add(num)
    return sum(n for n in candidates if n >= min_start and in_ranges(n, merged))

def part_two(lines):
    merged = parse_ranges(lines)
    max_end = merged[-1][1]
    min_start = merged[0][0]
    max_len = len(str(max_end))
    candidates = set()
    for pat_len in range(1, max_len + 1):
        pat_start = 10 ** (pat_len - 1)
        pat_end = 10 ** pat_len
        max_repeat = max_len // pat_len
        if max_repeat < 2:
            continue
        for pat in range(pat_start, pat_end):
            base = str(pat)
            for repeat in range(2, max_repeat + 1):
                num_str = base * repeat
                num = int(num_str)
                if len(num_str) > max_len or num > max_end:
                    break
                candidates.add(num)
    return sum(n for n in candidates if n >= min_start and in_ranges(n, merged))

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def get_ranges(lines):
    ranges = []
    for line in lines:
        if not line: continue
        parts = line.split(',')
        for p in parts:
            p = p.strip()
            if not p: continue
            if '-' in p:
                try:
                    start, end = p.split('-')
                    ranges.append((int(start), int(end)))
                except ValueError:
                    continue
    return ranges

def part_one(lines):
    ranges = get_ranges(lines)
    if not ranges:
        return 0

    min_range_val = min(r[0] for r in ranges)
    max_range_val = max(r[1] for r in ranges)
    max_len = len(str(max_range_val))

    invalid_ids = set()
    for d in range(1, (max_len // 2) + 1):
        start_p = 10**(d-1)
        end_p = 10**d - 1
        for p in range(start_p, end_p + 1):
            s_p = str(p)
            s_id = s_p + s_p
            val_id = int(s_id)
            if min_range_val <= val_id <= max_range_val:
                for r_start, r_end in ranges:
                    if r_start <= val_id <= r_end:
                        invalid_ids.add(val_id)
                        break
    return sum(invalid_ids)

def part_two(lines):
    ranges = get_ranges(lines)
    if not ranges:
        return 0

    min_range_val = min(r[0] for r in ranges)
    max_range_val = max(r[1] for r in ranges)
    max_len = len(str(max_range_val))

    invalid_ids = set()
    for total_len in range(2, max_len + 1):
        for d in range(1, total_len):
            if total_len % d == 0:
                k = total_len // d
                start_p = 10**(d-1)
                end_p = 10**d - 1
                for p in range(start_p, end_p + 1):
                    s_p = str(p)
                    s_id = s_p * k
                    val_id = int(s_id)
                    if min_range_val <= val_id <= max_range_val:
                        for r_start, r_end in ranges:
                            if r_start <= val_id <= r_end:
                                invalid_ids.add(val_id)
                                break
    return sum(invalid_ids)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

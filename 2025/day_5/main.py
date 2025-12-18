import sys
import os
from bisect import bisect_right

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _parse(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges: list[tuple[int, int]] = []
    ids: list[int] = []
    section = 0
    for line in lines:
        if not line:
            section = 1
            continue
        if section == 0:
            a, b = line.split("-", 1)
            lo, hi = int(a), int(b)
            if lo > hi:
                lo, hi = hi, lo
            ranges.append((lo, hi))
        else:
            ids.append(int(line))
    return ranges, ids


def _merge(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []
    ranges = sorted(ranges)
    merged = [ranges[0]]
    for lo, hi in ranges[1:]:
        plo, phi = merged[-1]
        if lo <= phi + 1:
            merged[-1] = (plo, max(phi, hi))
        else:
            merged.append((lo, hi))
    return merged


def _contains(merged: list[tuple[int, int]], value: int) -> bool:
    idx = bisect_right(merged, (value, 10**30)) - 1
    if idx < 0:
        return False
    lo, hi = merged[idx]
    return lo <= value <= hi


def part_one(lines):
    ranges, ids = _parse(lines)
    merged = _merge(ranges)
    return sum(1 for v in ids if _contains(merged, v))

def part_two(lines):
    ranges, _ = _parse(lines)
    merged = _merge(ranges)
    return sum(hi - lo + 1 for lo, hi in merged)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

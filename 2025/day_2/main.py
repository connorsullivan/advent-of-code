import sys
import os
from bisect import bisect_left, bisect_right

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _parse_ranges(lines: list[str]) -> list[tuple[int, int]]:
    blob = "".join(lines).strip().rstrip(",")
    if not blob:
        return []
    ranges: list[tuple[int, int]] = []
    for part in blob.split(","):
        part = part.strip()
        if not part:
            continue
        a, b = part.split("-", 1)
        lo, hi = int(a), int(b)
        if lo > hi:
            lo, hi = hi, lo
        ranges.append((lo, hi))
    return ranges


def _range_sum(sorted_values: list[int], prefix: list[int], lo: int, hi: int) -> int:
    left = bisect_left(sorted_values, lo)
    right = bisect_right(sorted_values, hi)
    return prefix[right] - prefix[left]


def _invalid_ids_exactly_twice(max_value: int) -> tuple[list[int], list[int]]:
    max_digits = len(str(max_value))
    values: list[int] = []
    for k in range(1, max_digits // 2 + 1):
        pow10 = 10**k
        start = 10 ** (k - 1)
        end = 10**k
        for base in range(start, end):
            n = base * pow10 + base
            if n <= max_value:
                values.append(n)
    values.sort()
    prefix = [0]
    s = 0
    for v in values:
        s += v
        prefix.append(s)
    return values, prefix


def _invalid_ids_repeated_at_least_twice(max_value: int) -> tuple[list[int], list[int]]:
    max_digits = len(str(max_value))
    values: set[int] = set()
    for k in range(1, max_digits + 1):
        start = 10 ** (k - 1)
        end = 10**k
        max_reps = max_digits // k
        if max_reps < 2:
            continue
        pow10k = 10**k
        for base in range(start, end):
            rep = base
            for _r in range(2, max_reps + 1):
                rep = rep * pow10k + base
                if rep <= max_value:
                    values.add(rep)
    sorted_values = sorted(values)
    prefix = [0]
    s = 0
    for v in sorted_values:
        s += v
        prefix.append(s)
    return sorted_values, prefix


def part_one(lines):
    ranges = _parse_ranges(lines)
    if not ranges:
        return 0
    max_value = max(hi for _, hi in ranges)
    values, prefix = _invalid_ids_exactly_twice(max_value)
    total = 0
    for lo, hi in ranges:
        total += _range_sum(values, prefix, lo, hi)
    return total

def part_two(lines):
    ranges = _parse_ranges(lines)
    if not ranges:
        return 0
    max_value = max(hi for _, hi in ranges)
    values, prefix = _invalid_ids_repeated_at_least_twice(max_value)
    total = 0
    for lo, hi in ranges:
        total += _range_sum(values, prefix, lo, hi)
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

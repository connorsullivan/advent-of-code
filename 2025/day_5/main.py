import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    """Parse input into ranges and available IDs."""
    ranges = []
    available = []
    in_ranges = True
    
    for line in lines:
        if not line:
            in_ranges = False
            continue
        if in_ranges:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        else:
            available.append(int(line))
    
    return ranges, available

def is_fresh(id_val, ranges):
    """Check if an ID is fresh (falls within any range)."""
    for start, end in ranges:
        if start <= id_val <= end:
            return True
    return False

def part_one(lines):
    """Count how many available IDs are fresh."""
    ranges, available = parse_input(lines)
    return sum(1 for id_val in available if is_fresh(id_val, ranges))

def merge_ranges(ranges):
    """Merge overlapping ranges."""
    if not ranges:
        return []
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # Overlapping or adjacent
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return merged

def part_two(lines):
    """Count total fresh IDs from the ranges."""
    ranges, _ = parse_input(lines)
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

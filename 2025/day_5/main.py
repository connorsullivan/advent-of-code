import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Count how many available ingredient IDs are fresh."""
    # Parse the input: ranges before blank line, IDs after
    blank_idx = lines.index('') if '' in lines else len(lines)
    
    # Parse fresh ranges
    ranges = []
    for i in range(blank_idx):
        parts = lines[i].split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))
    
    # Parse available IDs
    available_ids = []
    for i in range(blank_idx + 1, len(lines)):
        if lines[i]:
            available_ids.append(int(lines[i]))
    
    # Check which IDs are fresh
    fresh_count = 0
    for id_val in available_ids:
        for start, end in ranges:
            if start <= id_val <= end:
                fresh_count += 1
                break
    
    return fresh_count

def part_two(lines):
    """Count total unique ingredient IDs that are considered fresh by the ranges."""
    # Parse the input: ranges before blank line
    blank_idx = lines.index('') if '' in lines else len(lines)
    
    # Parse fresh ranges
    ranges = []
    for i in range(blank_idx):
        parts = lines[i].split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))
    
    # Merge overlapping ranges to count unique IDs
    if not ranges:
        return 0
    
    # Sort ranges by start
    ranges.sort()
    
    # Merge overlapping ranges
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        if start <= merged[-1][1] + 1:
            # Overlapping or adjacent, merge
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    # Count total IDs in merged ranges
    total = 0
    for start, end in merged:
        total += end - start + 1
    
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

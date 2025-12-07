import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def is_safe_report(levels):
    """Check if a report is safe according to the rules."""
    if len(levels) < 2:
        return True

    # Determine if increasing or decreasing based on first difference
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]

    # All differences must be positive (increasing) or all negative (decreasing)
    all_increasing = all(d > 0 for d in differences)
    all_decreasing = all(d < 0 for d in differences)

    if not (all_increasing or all_decreasing):
        return False

    # All differences must be between 1 and 3 in absolute value
    return all(1 <= abs(d) <= 3 for d in differences)

def part_one(lines):
    """Count safe reports."""
    safe_count = 0
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_report(levels):
            safe_count += 1
    return safe_count

def part_two(lines):
    """Count safe reports with Problem Dampener (can remove one level)."""
    safe_count = 0
    for line in lines:
        levels = list(map(int, line.split()))

        # Check if already safe
        if is_safe_report(levels):
            safe_count += 1
            continue

        # Try removing each level one at a time
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i+1:]
            if is_safe_report(modified_levels):
                safe_count += 1
                break

    return safe_count

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

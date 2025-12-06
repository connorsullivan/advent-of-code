import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    is_increasing = all(1 <= d <= 3 for d in diffs)
    is_decreasing = all(-3 <= d <= -1 for d in diffs)
    return is_increasing or is_decreasing

def part_one(lines):
    safe_count = 0
    for line in lines:
        if not line:
            continue
        report = list(map(int, line.split()))
        if is_safe(report):
            safe_count += 1
    return safe_count

def part_two(lines):
    safe_count = 0
    for line in lines:
        if not line:
            continue
        report = list(map(int, line.split()))

        if is_safe(report):
            safe_count += 1
        else:
            # Try removing one element
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    safe_count += 1
                    break
    return safe_count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))

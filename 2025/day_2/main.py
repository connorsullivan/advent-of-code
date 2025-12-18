import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def is_repeated_twice(n):
    """Check if number is a sequence of digits repeated exactly twice."""
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]

def is_repeated_at_least_twice(n):
    """Check if number is a sequence of digits repeated at least twice."""
    s = str(n)
    length = len(s)
    # Try all possible repeat lengths (1 to length//2)
    for repeat_len in range(1, length // 2 + 1):
        if length % repeat_len == 0:
            pattern = s[:repeat_len]
            if pattern * (length // repeat_len) == s:
                return True
    return False

def parse_ranges(lines):
    """Parse the input into a list of (start, end) tuples."""
    ranges = []
    text = ''.join(lines)
    for r in text.split(','):
        r = r.strip()
        if r and '-' in r:
            start, end = r.split('-')
            ranges.append((int(start), int(end)))
    return ranges

def part_one(lines):
    """Find all invalid IDs (repeated exactly twice) in the given ranges."""
    ranges = parse_ranges(lines)
    total = 0
    
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_repeated_twice(n):
                total += n
    
    return total

def part_two(lines):
    """Find all invalid IDs (repeated at least twice) in the given ranges."""
    ranges = parse_ranges(lines)
    total = 0
    
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_repeated_at_least_twice(n):
                total += n
    
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

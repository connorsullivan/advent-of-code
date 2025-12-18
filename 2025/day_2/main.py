import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def is_repeated_pattern(num_str, min_repeats=2, max_repeats=2):
    """Check if a number string is a pattern repeated exactly min_repeats to max_repeats times."""
    n = len(num_str)
    
    # Try each possible pattern length
    for pattern_len in range(1, n // min_repeats + 1):
        if n % pattern_len != 0:
            continue
        
        repeats = n // pattern_len
        if repeats < min_repeats or repeats > max_repeats:
            continue
        
        pattern = num_str[:pattern_len]
        if pattern[0] == '0':  # No leading zeros
            continue
        
        # Check if this pattern repeated gives us the number
        if pattern * repeats == num_str:
            return True
    
    return False

def part_one(lines):
    """Find invalid IDs that are a pattern repeated exactly twice."""
    import re
    # Parse the ranges from the single line
    ranges_str = lines[0] if lines else ""
    ranges = []
    for range_str in ranges_str.split(','):
        range_str = range_str.strip()
        if range_str:
            # Use regex to extract the two numbers
            nums = re.findall(r'\d+', range_str)
            if len(nums) == 2:
                start = int(nums[0])
                end = int(nums[1])
                ranges.append((start, end))
    
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            num_str = str(num)
            if is_repeated_pattern(num_str, min_repeats=2, max_repeats=2):
                total += num
    
    return total

def part_two(lines):
    """Find invalid IDs that are a pattern repeated at least twice."""
    import re
    # Parse the ranges from the single line
    ranges_str = lines[0] if lines else ""
    ranges = []
    for range_str in ranges_str.split(','):
        range_str = range_str.strip()
        if range_str:
            # Use regex to extract the two numbers
            nums = re.findall(r'\d+', range_str)
            if len(nums) == 2:
                start = int(nums[0])
                end = int(nums[1])
                ranges.append((start, end))
    
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            num_str = str(num)
            if is_repeated_pattern(num_str, min_repeats=2, max_repeats=len(num_str)):
                total += num
    
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

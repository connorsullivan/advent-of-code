import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def max_k_digit_greedy(line, k):
    """Find the maximum k-digit number by picking k digits from line in order."""
    n = len(line)
    result = []
    start = 0
    
    for i in range(k):
        # We need to pick (k - i) more digits
        # We can look ahead at most until position n - (k - i) + 1
        remaining = k - i
        max_pos = n - remaining
        
        # Find the maximum digit in the valid range
        max_digit = line[start]
        max_idx = start
        for j in range(start, max_pos + 1):
            if line[j] > max_digit:
                max_digit = line[j]
                max_idx = j
        
        result.append(max_digit)
        start = max_idx + 1
    
    return int(''.join(result))

def part_one(lines):
    """Find the maximum 2-digit joltage from each battery bank."""
    total = 0
    
    for line in lines:
        # Pick any 2 batteries (digits) to maximize the 2-digit number
        max_joltage = max_k_digit_greedy(line, 2)
        total += max_joltage
    
    return total

def part_two(lines):
    """Find the maximum 12-digit joltage from each battery bank."""
    total = 0
    
    for line in lines:
        # Pick any 12 batteries (digits) to maximize the 12-digit number
        max_joltage = max_k_digit_greedy(line, 12)
        total += max_joltage
    
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

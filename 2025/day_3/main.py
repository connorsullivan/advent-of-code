import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Find largest 2-digit joltage from each bank and sum them."""
    total = 0
    
    for line in lines:
        if not line:
            continue
        # Find the two highest digits and their positions
        max_joltage = 0
        n = len(line)
        for i in range(n):
            for j in range(i + 1, n):
                joltage = int(line[i] + line[j])
                max_joltage = max(max_joltage, joltage)
        total += max_joltage
    
    return total

def part_two(lines):
    """Find largest 12-digit joltage from each bank and sum them."""
    total = 0
    
    for line in lines:
        if not line:
            continue
        # We need to pick 12 batteries from the bank
        # To maximize the 12-digit number, we need to pick the largest digits
        # in the best positions (earlier digits matter more)
        # 
        # Strategy: greedily pick the largest digit we can at each position
        # while ensuring we have enough digits left
        n = len(line)
        if n < 12:
            continue
            
        # Greedy approach: at each step, pick the largest digit possible
        # from the range that still leaves enough digits for remaining positions
        result = []
        pos = 0
        for i in range(12):
            remaining_picks = 12 - i - 1  # How many more we need after this
            # We can pick from pos to n - remaining_picks - 1
            # Find the max digit in that range
            best_digit = '0'
            best_pos = pos
            for j in range(pos, n - remaining_picks):
                if line[j] > best_digit:
                    best_digit = line[j]
                    best_pos = j
            result.append(best_digit)
            pos = best_pos + 1
        
        joltage = int(''.join(result))
        total += joltage
    
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def solve_design(design, patterns, max_len):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for length in range(1, min(i, max_len) + 1):
            if dp[i - length] and design[i - length:i] in patterns:
                dp[i] = True
                break
    return dp[n]

def part_one(lines):
    patterns_line = lines[0]
    patterns = set(p.strip() for p in patterns_line.split(','))
    max_len = max(len(p) for p in patterns)

    designs = lines[2:]
    possible_count = 0

    for design in designs:
        if solve_design(design, patterns, max_len):
            possible_count += 1

    return possible_count

def count_ways(design, patterns, max_len):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for length in range(1, min(i, max_len) + 1):
            if design[i - length:i] in patterns:
                dp[i] += dp[i - length]
    return dp[n]

def part_two(lines):
    patterns_line = lines[0]
    patterns = set(p.strip() for p in patterns_line.split(','))
    max_len = max(len(p) for p in patterns)

    designs = lines[2:]
    total_ways = 0

    for design in designs:
        total_ways += count_ways(design, patterns, max_len)

    return total_ways

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))

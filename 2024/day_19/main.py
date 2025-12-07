import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    # Parse input
    patterns = [p.strip() for p in lines[0].split(',')]
    designs = [line.strip() for line in lines[2:] if line.strip()]

    def can_make_design(design, patterns):
        """Check if a design can be made using the available patterns."""
        n = len(design)
        # dp[i] = True if design[0:i] can be made
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be made

        for i in range(1, n + 1):
            for pattern in patterns:
                pattern_len = len(pattern)
                if i >= pattern_len and dp[i - pattern_len]:
                    if design[i - pattern_len:i] == pattern:
                        dp[i] = True
                        break

        return dp[n]

    possible_count = sum(1 for design in designs if can_make_design(design, patterns))
    return possible_count

def part_two(lines):
    # Parse input
    patterns = [p.strip() for p in lines[0].split(',')]
    designs = [line.strip() for line in lines[2:] if line.strip()]

    def count_ways(design, patterns):
        """Count the number of ways a design can be made using the available patterns."""
        n = len(design)
        # dp[i] = number of ways to make design[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # One way to make empty string

        for i in range(1, n + 1):
            for pattern in patterns:
                pattern_len = len(pattern)
                if i >= pattern_len:
                    if design[i - pattern_len:i] == pattern:
                        dp[i] += dp[i - pattern_len]

        return dp[n]

    total_ways = sum(count_ways(design, patterns) for design in designs)
    return total_ways

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

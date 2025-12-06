import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from collections import defaultdict

def next_secret(secret):
    # Step 1
    res = secret * 64
    secret = secret ^ res
    secret = secret % 16777216

    # Step 2
    res = secret // 32
    secret = secret ^ res
    secret = secret % 16777216

    # Step 3
    res = secret * 2048
    secret = secret ^ res
    secret = secret % 16777216

    return secret

def part_one(lines):
    total = 0
    for line in lines:
        secret = int(line.strip())
        for _ in range(2000):
            secret = next_secret(secret)
        total += secret
    return total

def part_two(lines):
    sequence_total_score = defaultdict(int)

    for line in lines:
        secret = int(line.strip())
        prices = [secret % 10]
        for _ in range(2000):
            secret = next_secret(secret)
            prices.append(secret % 10)

        changes = []
        for i in range(len(prices) - 1):
            changes.append(prices[i+1] - prices[i])

        seen_sequences = set()
        for i in range(len(changes) - 3):
            seq = tuple(changes[i:i+4])
            if seq not in seen_sequences:
                seen_sequences.add(seq)
                price = prices[i+4]
                sequence_total_score[seq] += price

    return max(sequence_total_score.values())

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))

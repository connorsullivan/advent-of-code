import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from collections import defaultdict

def mix(secret, value):
    """Mix a value into the secret number using XOR."""
    return secret ^ value

def prune(secret):
    """Prune the secret number using modulo 16777216."""
    return secret % 16777216

def next_secret(secret):
    """Generate the next secret number in the sequence."""
    # Step 1: Multiply by 64, mix, and prune
    secret = prune(mix(secret, secret * 64))

    # Step 2: Divide by 32 (integer division), mix, and prune
    secret = prune(mix(secret, secret // 32))

    # Step 3: Multiply by 2048, mix, and prune
    secret = prune(mix(secret, secret * 2048))

    return secret

def generate_secrets(initial, count):
    """Generate count secret numbers starting from initial."""
    secrets = [initial]
    secret = initial
    for _ in range(count):
        secret = next_secret(secret)
        secrets.append(secret)
    return secrets

def part_one(lines):
    """Sum the 2000th secret number for each buyer."""
    total = 0
    for line in lines:
        initial = int(line.strip())
        secret = initial
        # Generate 2000 secret numbers
        for _ in range(2000):
            secret = next_secret(secret)
        total += secret
    return total

def part_two(lines):
    """Find the sequence of 4 price changes that yields the most bananas."""
    # For each buyer, track all sequences and their first occurrence price
    all_sequences = defaultdict(int)

    for line in lines:
        initial = int(line.strip())

        # Generate 2000 secret numbers and their prices
        secrets = generate_secrets(initial, 2000)
        prices = [s % 10 for s in secrets]

        # Calculate changes
        changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]

        # Track sequences for this buyer (only count first occurrence)
        seen_sequences = set()

        # Look for sequences of 4 consecutive changes
        for i in range(len(changes) - 3):
            sequence = tuple(changes[i:i+4])
            if sequence not in seen_sequences:
                seen_sequences.add(sequence)
                # The price after this sequence is at index i+4
                price = prices[i+4]
                all_sequences[sequence] += price

    # Find the sequence with the maximum total bananas
    return max(all_sequences.values())

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

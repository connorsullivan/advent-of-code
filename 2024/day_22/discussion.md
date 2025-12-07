# Day 22 - Monkey Market

## Part One

The problem involves simulating pseudorandom secret number generation for monkey traders. Each secret number evolves through a specific process:

1. Multiply by 64, mix (XOR) with the secret, then prune (mod 16777216)
2. Divide by 32 (integer division), mix with the secret, then prune
3. Multiply by 2048, mix with the secret, then prune

### Implementation

- **mix(secret, value)**: Returns `secret ^ value` (bitwise XOR)
- **prune(secret)**: Returns `secret % 16777216`
- **next_secret(secret)**: Applies the three-step process to generate the next secret

For each buyer's initial secret number, I generate 2000 new secret numbers and sum them all up.

**Answer: 14119253575**

## Part Two

Part 2 requires finding the optimal sequence of 4 consecutive price changes that maximizes banana earnings across all buyers. Prices are the ones digit (last digit) of each secret number.

### Algorithm

1. For each buyer, generate 2000 secret numbers and extract prices (secret % 10)
2. Calculate the price changes between consecutive prices
3. For each sequence of 4 consecutive changes, track the price at which that sequence first occurs for each buyer
4. Use a dictionary to accumulate total bananas for each unique 4-change sequence across all buyers
5. Return the maximum total

### Key Insights

- Each buyer only sells once - we only count the **first occurrence** of each sequence for that buyer
- We need to track sequences globally across all buyers to find the one that yields the most total bananas
- A sequence of 4 changes leads to a price at index i+4 (after the 4 changes have occurred)

### Complexity

With ~1665 buyers, each generating 2000 secrets, we evaluate approximately 1665 × 1997 ≈ 3.3 million sequences. Using a defaultdict to track unique sequences efficiently handles the large search space.

**Answer: 1600**

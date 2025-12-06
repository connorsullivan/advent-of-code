# Day 22: Monkey Market

## Part 1

The problem asks us to simulate a pseudorandom number generator. The generator involves three steps, each modifying the "secret number" using bitwise XOR (`mix`) and modulo arithmetic (`prune`).

The process for generating the next secret number is:
1.  Multiply by 64, mix, prune.
2.  Divide by 32 (integer division), mix, prune.
3.  Multiply by 2048, mix, prune.

"Mix" is bitwise XOR. "Prune" is modulo 16777216 ($2^{24}$).

We need to simulate this process 2000 times for each initial secret number provided in the input and sum the 2000th secret number of each buyer.

### Complexity
*   **Time**: $O(N \times K)$, where $N$ is the number of buyers (lines in input) and $K$ is the number of iterations (2000).
*   **Space**: $O(1)$ if we just track the current secret number.

## Part 2

We need to find a sequence of 4 consecutive price changes that maximizes the total bananas we can get. The price is the ones digit of the secret number.

For each buyer, we generate the sequence of 2000 prices. We then calculate the changes between consecutive prices. We look for sequences of 4 changes. The first time a sequence appears for a buyer, we "sell" and get the current price (the price at the end of the sequence).

We want to find the single sequence of 4 changes that yields the highest total price across all buyers.

### Algorithm
1.  Initialize a map `sequence_total_score` to store the total price for each sequence.
2.  For each buyer:
    *   Generate 2000 secret numbers and extract prices (ones digit).
    *   Calculate the list of price changes.
    *   Iterate through the changes with a sliding window of size 4.
    *   For each window (sequence), if it hasn't been seen yet for this buyer:
        *   Add the corresponding price to `sequence_total_score` for that sequence.
        *   Mark the sequence as seen for this buyer.
3.  The answer is the maximum value in `sequence_total_score`.

### Complexity
*   **Time**: $O(N \times K)$, where $N$ is the number of buyers and $K$ is 2000. We iterate through the prices/changes once per buyer.
*   **Space**: $O(S)$, where $S$ is the number of unique sequences of 4 changes. Since changes are between -9 and 9, the number of sequences is bounded (at most $19^4 \approx 130,000$).

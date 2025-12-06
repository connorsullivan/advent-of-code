# Day 19: Linen Layout

## Part 1
The problem asks us to determine how many designs can be formed by concatenating available towel patterns. This is a variation of the "Word Break" problem.

I used Dynamic Programming (DP) to solve this.
Let `dp[i]` be a boolean indicating if the prefix of length `i` of the design can be formed.
`dp[0] = True` (empty string).
For each position `i` from 1 to `N` (length of design), we check all possible last patterns ending at `i`. If a pattern of length `L` matches the suffix `design[i-L:i]` and `dp[i-L]` is true, then `dp[i]` becomes true.

To optimize, I only check pattern lengths that exist in the input (or up to the maximum pattern length).

## Part 2
The second part asks for the total number of ways to form each design.

This requires a small modification to the DP state. Instead of a boolean, `dp[i]` stores the number of ways to form the prefix of length `i`.
`dp[0] = 1`.
For each position `i`, `dp[i]` is the sum of `dp[i-L]` for all valid patterns of length `L` that match the suffix.

The final answer is the sum of `dp[N]` for all designs.

## Complexity
- **Time Complexity**: For each design of length `N`, and maximum pattern length `M`, the complexity is `O(N * M)`. Since `M` is small (length of towel patterns), this is efficient.
- **Space Complexity**: `O(N)` for the DP array for each design.

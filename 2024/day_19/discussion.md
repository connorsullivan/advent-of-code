# Day 19: Linen Layout

## Part One

**Problem**: Given a set of available towel patterns (strings of colored stripes), determine how many desired designs can be created by combining these patterns in sequence.

**Approach**: This is a classic dynamic programming problem similar to word break problems.

- Parse the input to extract available patterns and desired designs
- For each design, use DP to check if it can be formed:
  - `dp[i]` represents whether `design[0:i]` can be made
  - `dp[0] = True` (empty string is always possible)
  - For each position `i`, check all patterns to see if they match ending at position `i`
  - If `design[i-len(pattern):i]` matches a pattern AND `dp[i-len(pattern)]` is true, then `dp[i] = True`
- Count how many designs have `dp[n] = True`

**Result**: 263 designs are possible

**Time Complexity**: O(D × N × P) where D is number of designs, N is average design length, P is number of patterns

## Part Two

**Problem**: For each possible design, count the total number of different ways it can be arranged using the available patterns.

**Approach**: Similar to Part One, but instead of boolean values, we track the count of ways:

- `dp[i]` now represents the number of ways to make `design[0:i]`
- `dp[0] = 1` (one way to make empty string)
- For each position `i`, for each matching pattern:
  - If `design[i-len(pattern):i]` matches a pattern, add `dp[i-len(pattern)]` to `dp[i]`
  - This accumulates all possible ways to reach position `i`
- Sum up `dp[n]` for all designs

**Result**: 723,524,534,506,343 total arrangements

**Time Complexity**: O(D × N × P) where D is number of designs, N is average design length, P is number of patterns

## Key Insights

1. **Dynamic Programming**: Both parts use DP with overlapping subproblems - once we know if/how many ways we can make a prefix, we can use that to build longer prefixes
2. **Pattern Matching**: We check each pattern against substrings of the design, building up from left to right
3. **Accumulation**: Part 2 accumulates counts rather than using boolean flags, allowing us to count all possible combinations
4. **Efficiency**: The DP approach avoids exponential recursion by memoizing results for each position

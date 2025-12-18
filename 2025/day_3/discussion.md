# Day 3

## Part One

The problem involves battery banks where each line is a string of digit values (1-9). We need to select exactly 2 batteries (digits) from each bank to form a 2-digit number, maximizing the joltage output. The selected batteries must maintain their original order.

The solution uses a greedy algorithm:
1. For each position to fill in the result, look ahead in the valid range
2. Pick the largest available digit while ensuring enough digits remain for subsequent positions
3. The valid range for position i is from current_start to (n - remaining_digits_needed)

For 2 digits, this is simple: pick the largest digit from positions 0 to n-2, then pick the largest from the remaining positions.

Time complexity: O(n × m × k) where n is the number of banks, m is the average bank length, and k is the number of digits to select.

## Part Two

Part two extends the problem to selecting exactly 12 batteries instead of 2. The same greedy algorithm applies but with k=12.

The greedy approach works because:
- We want the lexicographically largest subsequence of length k
- At each step, we pick the largest digit that still allows us to select enough remaining digits
- This ensures the most significant positions have the largest possible values

Time complexity: Same as part one, but with k=12 instead of k=2.

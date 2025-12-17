# Day 3

## Part One
The problem asks for the largest 2-digit number that can be formed by picking two batteries (digits) from each bank while preserving their relative order. This is equivalent to finding the largest subsequence of length 2.

The approach used is a greedy algorithm with a monotonic stack:
1. Maintain a stack of digits.
2. Iterate through the digits of the bank.
3. While the current digit is greater than the top of the stack and we still have enough digits left to remove (to maintain the required length), pop from the stack.
4. Push the current digit.
5. The first 2 digits of the stack form the maximum joltage for that bank.

The total joltage is the sum of these maximums across all banks.

## Part Two
Part Two is identical to Part One, but instead of picking 2 batteries, we need to pick exactly 12. The same greedy monotonic stack algorithm works perfectly for any length $k$, as long as $k \le$ length of the input string.

The algorithm ensures that we always keep the largest possible digits in the most significant positions, provided we have enough remaining digits to complete the subsequence of length $k$.

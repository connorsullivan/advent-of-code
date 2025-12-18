# Day 2

## Part One

The problem asks us to find "invalid" product IDs in given ranges. An invalid ID is one where the number is composed of a pattern repeated exactly twice (e.g., 11 = "1" × 2, 1010 = "10" × 2, 222222 = "222" × 2).

The solution:
1. Parse comma-separated ranges from the input
2. For each range, iterate through all numbers
3. Check if each number can be expressed as a pattern repeated exactly twice
4. Sum all invalid IDs

The pattern checking works by trying all possible pattern lengths (from 1 to half the number's length), checking if the number length is divisible by the pattern length, and verifying the pattern doesn't have leading zeros.

Time complexity: O(n × m × d) where n is the number of ranges, m is the average range size, and d is the average number of digits.

## Part Two

Part two extends the definition: an invalid ID is now any number that is a pattern repeated at least twice (not just exactly twice). For example, 111 = "1" × 3, 12341234 = "1234" × 2, etc.

The solution is the same as part one, but we check for patterns repeated from 2 times up to the full length of the number (instead of exactly 2 times).

Time complexity: Same as part one.

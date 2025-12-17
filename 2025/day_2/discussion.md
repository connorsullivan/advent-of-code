# Day 2

## Part One
The problem asks to find the sum of all "invalid" IDs within given ranges. An ID is invalid if it consists of a sequence of digits repeated exactly twice (e.g., `123123`).

### Approach
Instead of iterating through every number in the ranges, which could be millions, I generated all possible invalid IDs and checked if they fell within any of the ranges.
- For each possible length $d$ of the repeating sequence $P$ (from 1 to 5, since the maximum ID length is 10), I generated all $P$ values that do not start with zero.
- Formed the ID by concatenating $P$ with itself.
- Checked if the resulting ID was within any of the input ranges.
- Summed the unique invalid IDs found.

## Part Two
The rule for invalid IDs is expanded: an ID is invalid if it consists of a sequence of digits repeated at least twice (e.g., `121212`, `111`).

### Approach
Similar to Part 1, I generated all possible invalid IDs:
- For each total length $L$ from 2 to 10:
  - For each divisor $d$ of $L$ such that $d < L$:
    - Generated all sequences $P$ of length $d$ that do not start with zero.
    - Formed the ID by repeating $P$ exactly $L/d$ times.
    - Checked if the ID was within any of the input ranges.
- Used a set to ensure each unique invalid ID was counted only once.
- Summed the unique invalid IDs.

This generation approach is much more efficient than brute-force iteration, as there are only about 100,000 possible invalid IDs to check against the 40 ranges.

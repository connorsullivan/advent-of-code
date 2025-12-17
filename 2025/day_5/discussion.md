# Day 5

## Part One
The problem asks to count how many available ingredient IDs fall within any of the given fresh ID ranges.
The input consists of two sections separated by a blank line:
1. A list of fresh ingredient ID ranges (e.g., `3-5`).
2. A list of available ingredient IDs.

The ranges are inclusive. For each available ID, we iterate through the ranges and check if the ID is greater than or equal to the start and less than or equal to the end of any range. If it matches at least one range, it is counted as fresh.

## Part Two
The problem asks for the total number of unique ingredient IDs that are considered fresh according to the ranges.
Since the ranges can overlap, we cannot simply sum their lengths. Instead, we:
1. Sort the ranges by their starting values.
2. Merge overlapping or adjacent ranges. Two ranges $[s_1, e_1]$ and $[s_2, e_2]$ (where $s_1 \le s_2$) can be merged if $s_2 \le e_1 + 1$. The merged range will be $[s_1, \max(e_1, e_2)]$.
3. Sum the number of IDs in each merged disjoint range using the formula $(end - start + 1)$.

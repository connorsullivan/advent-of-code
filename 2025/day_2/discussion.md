# Day 2

## Part One
Merge the input ranges, then generate every number made of a digit sequence repeated exactly twice. Since the longest value fits in the widest input range, iterate over each even length, build candidates by repeating the left half, and sum those that fall into any merged interval.

## Part Two
Extend the candidate generation so a number is valid if some digit sequence repeats two or more times. For each pattern length and repeat count that keeps the total length within the longest range, repeat the pattern to form a number. Deduplicate candidates with a set and sum those contained in the merged ranges.

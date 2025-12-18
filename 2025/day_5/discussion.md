# Day 5

## Part One

The problem involves checking which ingredient IDs from a given list fall within specified "fresh" ranges. The input has two sections separated by a blank line: fresh ingredient ID ranges and available ingredient IDs.

The solution:
1. Parse the ranges (inclusive) from the first section
2. Parse the available IDs from the second section
3. For each available ID, check if it falls within any range
4. Count how many IDs are fresh

Time complexity: O(n × r) where n is the number of available IDs and r is the number of ranges.

## Part Two

Part two asks for the total count of unique IDs that are considered fresh by the ranges, ignoring the available IDs list entirely.

The solution:
1. Parse only the ranges from the first section
2. Sort ranges by start position
3. Merge overlapping or adjacent ranges
4. Sum the size of each merged range (end - start + 1)

The key insight is that overlapping ranges like [10-14] and [12-18] should be merged into [10-18] to avoid double-counting IDs.

Time complexity: O(r log r) for sorting, where r is the number of ranges.

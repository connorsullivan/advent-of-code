# Day 2: Red-Nosed Reports

## Part One

The problem asks us to determine how many reports are "safe" based on two criteria:
1. All levels must be either strictly increasing or strictly decreasing
2. Adjacent levels must differ by at least 1 and at most 3

### Approach
I implemented an `is_safe_report()` helper function that:
1. Calculates all differences between adjacent levels
2. Checks if all differences are positive (increasing) or all negative (decreasing)
3. Verifies that all absolute differences are between 1 and 3

For each line in the input, I parse the levels as integers and check if the report is safe.

**Answer: 371 safe reports**

## Part Two

Part Two introduces the "Problem Dampener" - a mechanism that allows a report to be considered safe if removing any single level would make it safe.

### Approach
For each report:
1. First check if it's already safe (no removal needed)
2. If not safe, try removing each level one at a time
3. Check if any of these modified reports would be safe
4. Count the report as safe if any removal works

This brute-force approach works well since each report is small (typically 5-8 levels). The time complexity is O(n²) per report where n is the number of levels, but with small n this is efficient.

**Answer: 426 safe reports**

### Key Insights
- Part 1 is straightforward validation logic
- Part 2 requires trying all possible single-level removals
- The "Problem Dampener" significantly increases the number of safe reports (from 371 to 426)
- Edge cases to consider: reports with only 2 levels, all identical values, or extreme jumps

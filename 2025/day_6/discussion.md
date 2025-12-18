# Day 6

## Part One

The worksheet is a fixed-width ASCII grid with multiple “problems” placed side-by-side.
Problems are separated by at least one full column of spaces.

Parsing:

- read the input **without stripping spaces**
- pad all rows to equal width
- find separator columns (all spaces in every row)
- slice each contiguous non-separator column block as one problem

For part one, each row (except the last operator row) contains one number; within a problem block we extract the digits from that row to form the number.
Then we apply the operator (`+` or `*`) and sum all problem results.

## Part Two

Cephalopod math uses columns as numbers, read right-to-left.
Within a problem block, for each column (from rightmost to leftmost), we read digits top-to-bottom (skipping spaces) to form the number in that column.
Then we apply the operator to those numbers and sum across all problems.

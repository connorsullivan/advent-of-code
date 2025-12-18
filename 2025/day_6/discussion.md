# Day 6

## Part One
Keep the exact spacing from the worksheet by reading the raw input. Pad every line to the same width, find columns that are entirely spaces, and treat contiguous non-space columns as individual problems. For each problem block, strip the numeric rows into integers, read the operator from the bottom row, and apply either sum or product before adding to the grand total.

## Part Two
Problems are still separated by all-space columns, but numbers are now given vertically. For each block, scan its columns from right to left, building each number from the non-space digits in that column (top to bottom). Combine these numbers with the operator exactly as before to accumulate the grand total.

# Day 6

## Part One
The problem involves reading a grid of numbers and operators. Numbers are arranged vertically in columns, and problems are separated by columns of spaces. At the bottom of each problem is an operator (+ or *).

My approach:
1.  Identify "blocks" of columns separated by space-only columns.
2.  For each block, the last row contains the operator.
3.  Each other row in the block represents a number. I extracted the string for each row within the block's column range, stripped spaces, and parsed it as an integer.
4.  Applied the operator to all numbers in the block using `functools.reduce`.
5.  Summed the results of all problems.

## Part Two
The rules for reading the math changed. Now, each column within a block represents a single number, read from top to bottom. The problems are read from right to left.

My approach:
1.  Used the same block identification as Part 1.
2.  For each block, iterated through the columns from right to left.
3.  For each column, concatenated the digits from top to bottom (excluding the last row) and parsed as an integer.
4.  Applied the operator to these numbers.
5.  Summed the results of all problems.

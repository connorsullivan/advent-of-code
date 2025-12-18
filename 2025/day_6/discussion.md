# Day 6

## Part One

The problem involves solving math problems arranged in a grid. Each problem consists of numbers arranged vertically in columns, with an operator at the bottom. Problems are separated by columns of spaces. Reading left-to-right, we extract numbers row-by-row and apply the operator.

The solution:
1. Parse the grid to identify problem boundaries (separated by all-space columns)
2. For each problem, read rows top-to-bottom, extracting numbers and the operator
3. Apply the operator to all numbers in sequence (left-to-right associative)
4. Sum all problem results to get the grand total

Time complexity: O(rows × cols) to parse the grid and identify problems.

## Part Two

Part two reveals that cephalopod math is read right-to-left by columns. Each single-character column forms a number by reading top-to-bottom (most significant digit at top). The operator is in the column that contains it (often with digits too).

The solution:
1. Parse problem boundaries the same way
2. For each problem, process columns right-to-left instead of rows top-to-bottom
3. Each column is read top-to-bottom to form a number
4. If a column contains an operator (+, *), extract both the operator and any digits in that column
5. Apply the operator and sum results

The key insight is understanding that a single column can contain both digits and an operator (e.g., '623+' is a column with digits 6, 2, 3, and +).

Time complexity: Same as part one, O(rows × cols).

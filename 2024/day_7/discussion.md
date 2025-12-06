# Day 7: Bridge Repair

## Problem Description

We are given a list of calibration equations. Each equation consists of a target test value and a list of numbers. We need to determine if we can insert operators between the numbers to produce the target value. The operators are evaluated left-to-right.

### Part 1
Allowed operators:
- Addition (`+`)
- Multiplication (`*`)

### Part 2
Allowed operators:
- Addition (`+`)
- Multiplication (`*`)
- Concatenation (`||`) - joins digits (e.g., `12 || 345` -> `12345`)

## Solution Approach

I used a recursive backtracking approach (Depth First Search) to explore all possible operator combinations.

### Algorithm

For each equation:
1.  Start with the first number as the `current_value`.
2.  Recursively process the remaining numbers one by one.
3.  At each step, apply all allowed operators to the `current_value` and the next number.
4.  If the `current_value` exceeds the target value, prune the branch (since all numbers are positive and operators only increase the value).
5.  If we reach the end of the numbers and `current_value` equals the target, the equation is valid.

### Complexity Analysis

Let $N$ be the number of operands in an equation.
- **Part 1**: There are $N-1$ operator slots, each with 2 choices. Time complexity is $O(2^N)$ per equation.
- **Part 2**: There are $N-1$ operator slots, each with 3 choices. Time complexity is $O(3^N)$ per equation.

Given the input size (number of lines and number of operands per line), this exponential complexity is acceptable. The pruning optimization helps significantly.

### Implementation Details

- **Concatenation**: Implemented using string conversion: `int(str(a) + str(b))`.
- **Pruning**: `if current_val > target: return False` is crucial for performance.

## Results

- **Part 1 Answer**: 42283209483350
- **Part 2 Answer**: 1026766857276279

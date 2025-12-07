# Day 7: Bridge Repair

## Problem Summary

The task involves calibrating equations where we need to determine if a test value can be produced by inserting operators between a sequence of numbers. The operators are evaluated strictly left-to-right (no precedence rules).

## Part One

**Operators Available**: Addition (`+`) and Multiplication (`*`)

### Approach

1. **Parse Input**: Each line contains a test value (before colon) and a list of numbers (after colon)
2. **Generate Combinations**: For n numbers, we need n-1 operators. Use `itertools.product` to generate all possible combinations of `+` and `*`
3. **Evaluate Left-to-Right**: For each operator combination, evaluate the expression from left to right
4. **Check Validity**: If any combination produces the test value, include it in the sum
5. **Sum Valid Equations**: Return the sum of all test values that can be produced

### Key Insights

- With n-1 operator positions and 2 operators, there are 2^(n-1) possible combinations
- Left-to-right evaluation means `81 + 40 * 27` = `(81 + 40) * 27` = `3267`, not `81 + 1080`
- Brute force is feasible for reasonable input sizes

**Answer**: 3,245,122,495,150

## Part Two

**Additional Operator**: Concatenation (`||`) which combines digits (e.g., `12 || 345 = 12345`)

### Approach

Same algorithm as Part One, but now with 3 operators instead of 2:
- For n-1 operator positions, there are now 3^(n-1) possible combinations
- The concatenation operator joins the string representations of two numbers

### Key Insights

- Concatenation creates larger numbers quickly, enabling more possible target values
- The search space grows exponentially (3^(n-1) vs 2^(n-1)), but still manageable
- Examples from problem:
  - `15 || 6 = 156`
  - `6 * 8 || 6 * 15 = 48 || 6 * 15 = 486 * 15 = 7290`
  - `17 || 8 + 14 = 178 + 14 = 192`

**Answer**: 105,517,128,211,543

## Implementation Notes

- Used `itertools.product` to generate all operator combinations efficiently
- Implemented left-to-right evaluation in a simple loop
- Concatenation implemented by converting to strings and back to integers
- Solution validates correctly against provided sample data before running on full input

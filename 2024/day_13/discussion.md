# Day 13: Claw Contraption

## Problem Description

We are given a list of claw machines. Each machine has two buttons, A and B.
- Button A moves the claw by $(X_A, Y_A)$ and costs 3 tokens.
- Button B moves the claw by $(X_B, Y_B)$ and costs 1 token.
- There is a prize at $(X_P, Y_P)$.

We need to find the number of presses $A$ and $B$ such that:
$$ A \cdot X_A + B \cdot X_B = X_P $$
$$ A \cdot Y_A + B \cdot Y_B = Y_P $$

We want to minimize the cost $3A + B$.

### Part 1
The prize locations are small, and we are told that $A, B \le 100$.

### Part 2
The prize locations are shifted by $10^{13}$ on both axes. The 100 press limit is removed.

## Solution Approach

This is a system of two linear equations with two variables ($A$ and $B$).
We can solve this system using Cramer's Rule or simple substitution.

The determinant of the coefficient matrix is:
$$ D = X_A \cdot Y_B - X_B \cdot Y_A $$

The solutions for $A$ and $B$ are:
$$ A = \frac{X_P \cdot Y_B - X_B \cdot Y_P}{D} $$
$$ B = \frac{X_A \cdot Y_P - X_P \cdot Y_A}{D} $$

For a valid solution:
1. The determinant $D$ must be non-zero (if $D=0$, the vectors are parallel).
2. The calculated $A$ and $B$ must be integers (i.e., the numerators must be divisible by $D$).
3. $A$ and $B$ must be non-negative.

Since we have a system of linear equations with a unique solution (when $D \neq 0$), there is only one pair $(A, B)$ that satisfies the position requirement. We don't need to search for a minimum cost because there is no choice in $A$ and $B$ to reach the target exactly, unless the vectors are collinear (which implies $D=0$). In the input data, the vectors are generally not collinear.

### Complexity
- **Time Complexity**: $O(N)$, where $N$ is the number of machines. Solving the equation for each machine takes $O(1)$ time.
- **Space Complexity**: $O(N)$ to store the input, or $O(1)$ if processed as a stream.

## Implementation Details
- Used Python's arbitrary precision integers to handle the large numbers in Part 2.
- Implemented a parser to extract coordinates using regular expressions.
- Applied the offset of $10^{13}$ for Part 2.

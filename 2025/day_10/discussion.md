# Day 10

## Part One
The problem asks for the minimum number of button presses to reach a target configuration of indicator lights. Each button toggles a set of lights. This can be modeled as a system of linear equations over the field $GF(2)$.
- Each button is a vector in $GF(2)^n$.
- The target configuration is a vector $b \in GF(2)^n$.
- We want to find $x \in \{0, 1\}^n$ such that $Ax = b \pmod 2$ and $\sum x_i$ is minimized.
Since each button can only be pressed 0 or 1 times (pressing twice is equivalent to not pressing), we solve the system using Gaussian elimination. If there are free variables (null space), we iterate through all $2^k$ possible solutions to find the one with the minimum Hamming weight.

## Part Two
In Part Two, buttons increase joltage counters by 1 instead of toggling lights. We need to find the minimum total presses to reach exact joltage requirements. This is a system of linear equations over non-negative integers:
- $Ax = b$ where $x_i \in \mathbb{Z}_{\ge 0}$.
- Minimize $\sum x_i$.
Given the small number of buttons (up to 13) and counters (up to 10), the system is either uniquely solvable or has very few free variables (at most 3 in the provided input).
We use Gaussian elimination over the field of rational numbers ($\mathbb{Q}$) to find the general solution in terms of free variables. Then, we iterate over the possible values of the free variables (bounded by the target joltage levels) and check if the resulting pivot variables are non-negative integers. The solution with the minimum sum is our answer.

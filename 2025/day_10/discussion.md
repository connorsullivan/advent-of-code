# Day 10

## Part One

Each machine is an “XOR button” system:

- indicator lights are bits
- each button press toggles a subset of bits (XOR with a bitmask)

Pressing a button twice cancels out, so the optimal solution only uses each button 0 or 1 times.
With up to 10 lights, we can BFS in the `2^n` state space to find the minimum number of presses to reach the target bitmask.

## Part Two

In joltage mode, each press *adds* 1 to each listed counter, so we need a nonnegative integer solution to:

`A x = b`, minimizing `sum(x)`

For these inputs, each machine has at most 10 counters and the number of buttons is at most 3 larger than the number of counters, so the system has at most 3 free variables.

We solve each machine by:

- building the `0/1` matrix `A`
- computing a reduced row echelon form (RREF) over exact rational numbers
- enumerating integer values for the (≤3) free variables (bounded by per-button upper bounds)
- computing the implied pivot variables and keeping the feasible solution with the smallest total presses

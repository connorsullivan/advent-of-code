# Day 10

## Part One
Extract the indicator target pattern and button wiring from each line. Represent the desired light state and each button as bitmasks; pressing a button XORs its mask. With at most 13 buttons, brute-force every combination (0/1 press per button), track how many presses are used, and keep the minimum that produces the target mask. Sum the minima across all machines.

## Part Two
Counters are integers instead of bits. Parse the button effects as 0/1 vectors and the goal counts from the braces. Build the linear system \(A x = t\) (counters × buttons) where pressing a button adds 1 to each listed counter. Use Gauss–Jordan elimination to express pivot variables in terms of at most three free variables. For each feasible integer assignment of the free variables within natural bounds (no counter can be overfilled), compute the implied pivot values; if all are non-negative integers, this gives a valid solution. Track the minimal total presses across all feasible assignments for each machine and sum them.

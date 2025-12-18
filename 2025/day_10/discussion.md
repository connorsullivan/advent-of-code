# Day 10

## Part One
Extract the indicator target pattern and button wiring from each line. Represent the desired light state and each button as bitmasks; pressing a button XORs its mask. With at most 13 buttons, brute-force every combination (0/1 press per button), track how many presses are used, and keep the minimum that produces the target mask. Sum the minima across all machines.

## Part Two
Counters are integers instead of bits. Parse the button effects as 0/1 vectors and the goal counts from the braces. Model the problem as a shortest-path search from the target counts down to all zeros where pressing a button subtracts its vector (only allowed when no counter would go negative). Use an A* search with a simple admissible heuristic based on the maximum counters reduced in a single press to find the minimal press count for each machine, then sum the results.

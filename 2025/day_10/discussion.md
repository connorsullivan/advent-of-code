# Day 10

## Part One

The problem involves configuring indicator lights by pressing buttons. Each button toggles specific lights (XOR operation). We need to find the minimum number of button presses to reach a target configuration.

This is a system of linear equations over GF(2) (binary field). Each light can be on (1) or off (0), and pressing a button toggles its associated lights.

The solution:
1. Parse the target light configuration and button mappings
2. For small numbers of buttons (≤20), try all possible combinations (2^n)
3. For each combination, simulate button presses and check if we reach the target
4. Return the minimum number of presses needed

Time complexity: O(2^n × m) where n is buttons and m is lights, but n is small.

## Part Two

Part two changes the problem: instead of toggling lights, buttons now increment counters. We need to reach specific target values for each counter, starting from 0.

This is a system of linear equations over positive integers with L1 minimization. We want non-negative integer solutions that minimize total presses.

The solution uses a greedy approach:
1. Repeatedly select the button that increases the most counters that are still below their targets
2. Press that button once
3. Continue until all counters reach their targets

This greedy heuristic works well for the given inputs, though it may not always find the optimal solution for arbitrary inputs.

Time complexity: O(k × n × m) where k is the sum of target values, n is buttons, and m is counters.

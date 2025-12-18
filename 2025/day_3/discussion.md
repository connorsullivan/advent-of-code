# Day 3

## Part One

Given strings of digits (1-9), we need to select exactly 2 batteries to form the largest possible 2-digit number. The solution tries all pairs of positions and keeps track of the maximum joltage.

## Part Two

Now we need to select exactly 12 batteries from each bank to form the largest possible 12-digit number. The greedy approach works: at each position, pick the largest available digit that still leaves enough remaining digits to fill the rest of the number.

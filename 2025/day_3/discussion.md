# Day 3

## Part One
For each bank of digits, compute the best two-digit number you can make while keeping digit order. Track the maximum digit to the right of every position, then combine each digit with the best possible trailing digit; sum the best value for every bank.

## Part Two
Select the lexicographically largest subsequence of length 12 from each digit string. Use the standard greedy stack approach: while a larger upcoming digit exists and the stack can shrink, pop smaller digits; otherwise push if the stack still needs digits. Convert the resulting stack to an integer and sum across all banks.

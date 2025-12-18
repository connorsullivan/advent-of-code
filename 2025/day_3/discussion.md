# Day 3

## Part One

For each bank (a line of digits), we must pick two positions `i < j` to maximize the 2-digit number.
For each `i`, the best possible `j` is the maximum digit that appears to the right of `i`.

Compute a suffix maximum array and take:

`max(d[i] * 10 + suffix_max[i+1])`

Sum these maxima across all banks.

## Part Two

Now we must pick exactly 12 digits (in order) to form the largest 12-digit number.
This is the classic “remove `n-k` digits to maximize” greedy:

- maintain a stack of chosen digits
- while the next digit is larger and we still can remove digits, pop
- push the next digit

The stack’s first 12 digits are the maximum subsequence.

# Day 2

## Part One

An ID is invalid if it is a decimal string repeated twice, like `6464 = "64" + "64"`.
With a maximum input value of 10 digits, there are only:

`9 + 90 + 900 + 9000 + 90000 = 111105`

such IDs (choose the first half, then concatenate it with itself).

So we:

- parse all input ranges
- precompute every “double” invalid ID up to the maximum range end
- sort them and build a prefix sum
- answer each range query with two binary searches

## Part Two

Now an ID is invalid if it’s any repeated block at least twice (e.g. `"12"` repeated 5 times).
With up to 10 digits, enumerating all `block_len` and repeat counts still produces only ~100k candidates.

We generate all repeated IDs `<= max_value`, sort them, prefix-sum them, and sum each range with binary search.

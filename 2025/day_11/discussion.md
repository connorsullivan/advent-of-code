# Day 11

## Part One

We have a directed graph of devices. The task is to count all directed paths from `you` to `out`.

Assuming the graph is acyclic for the reachable portion (as intended by the puzzle), we can count paths with memoized DFS:

- `paths(out) = 1`
- `paths(node) = sum(paths(child) for child in outputs)`

The implementation also detects cycles on reachable paths to avoid infinite recursion.

## Part Two

Now we count paths from `svr` to `out` that visit both `dac` and `fft` (in any order).
This is the same DAG path counting, but with an extra 2-bit state:

- bit 0: have we visited `dac`?
- bit 1: have we visited `fft`?

We memoize `paths(node, seen_mask)` and only count a path as valid at `out` if `seen_mask == 3`.

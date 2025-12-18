# Day 11

## Part One
Parse the directed graph from the `source: neighbors` lines. Use a memoized DFS counting paths from `you` to `out`; each node’s path count is the sum of its neighbors’ counts, with `out` contributing 1.

## Part Two
Reuse the graph but track whether `dac` and `fft` have been visited. Memoize by `(node, seen_dac, seen_fft)` and only count a path when it reaches `out` with both flags set. Start from `svr` with both flags false.

# Day 11

## Part One
The problem asks for the number of different paths from a starting node `you` to an ending node `out` in a directed graph. The input specifies the outputs for each device. Since the problem states that data only flows through outputs and cannot flow backwards, the graph is a Directed Acyclic Graph (DAG).

I implemented a recursive path-counting function with memoization. For any node $u$, the number of paths to the target $T$ is the sum of the number of paths from each of its neighbors $v$ to $T$:
$$P(u, T) = \sum_{v \in \text{outputs}(u)} P(v, T)$$
Base cases:
- If $u = T$, $P(u, T) = 1$.
- If $u$ has no outputs and $u \neq T$, $P(u, T) = 0$.

## Part Two
Part Two asks for the number of paths from `svr` to `out` that visit both `dac` and `fft`. In a DAG, if a path visits two nodes $A$ and $B$, it must visit them in a fixed order (either $A$ then $B$, or $B$ then $A$).

The total number of paths visiting both is the sum of:
1. Paths visiting `dac` then `fft`: $P(\text{svr}, \text{dac}) \times P(\text{dac}, \text{fft}) \times P(\text{fft}, \text{out})$
2. Paths visiting `fft` then `dac`: $P(\text{svr}, \text{fft}) \times P(\text{fft}, \text{dac}) \times P(\text{dac}, \text{out})$

Since the graph is a DAG, these two sets of paths are disjoint. I used the same memoized path-counting function to calculate these components.

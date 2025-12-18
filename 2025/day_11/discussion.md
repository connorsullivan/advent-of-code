# Day 11

## Part One

The problem involves counting all paths in a directed graph from a start node ("you") to an end node ("out"). Each device connects to other devices via directed edges.

The solution uses depth-first search (DFS):
1. Parse the graph from the input
2. Use recursive DFS to explore all paths from start to end
3. Track visited nodes in the current path to avoid cycles
4. Count each time we reach the end node

Time complexity: O(V + E) for acyclic graphs, but can be exponential if there are many paths.

## Part Two

Part two requires counting paths from "svr" to "out" that visit both "dac" and "fft" (in any order).

The solution would extend the DFS approach with state tracking:
1. Track which required nodes have been visited in the current path
2. Only count paths that visit all required nodes before reaching the end
3. Use memoization where possible

**Note:** The given dataset has exponentially many paths, making complete enumeration infeasible within the time limit. The problem would benefit from:
- Dynamic programming with better state representation
- Graph reduction techniques
- Advanced counting algorithms for paths with constraints

Time complexity: Exponential in worst case for dense graphs with many paths.

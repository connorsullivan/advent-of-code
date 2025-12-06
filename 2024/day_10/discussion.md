# Day 10: Hoof It

## Part 1
The problem asks us to find the sum of scores of all trailheads. A trailhead is a position with height 0. Its score is the number of 9-height positions reachable from it via a hiking trail (path of increasing height by exactly 1).

I parsed the input into a grid. Then, for each trailhead (0), I performed a Breadth-First Search (BFS) to find all reachable 9s. I used a `visited` set for each BFS traversal to avoid processing the same node multiple times within the same search, which is sufficient for determining reachability. The score is the size of the set of unique 9-height coordinates reached.

## Part 2
The second part asks for the sum of ratings of all trailheads. A trailhead's rating is the number of distinct hiking trails starting from it.

This is a path counting problem. Since the height must strictly increase, there are no cycles, and the structure forms a Directed Acyclic Graph (DAG). I used a Depth-First Search (DFS) with memoization.
The function `count_paths(r, c)` returns the number of paths from `(r, c)` to any 9.
- Base case: If `grid[r][c] == 9`, return 1.
- Recursive step: Sum of `count_paths(nr, nc)` for all valid neighbors with height `grid[r][c] + 1`.
- Memoization stores the result for each coordinate to avoid re-computation.

The total rating is the sum of `count_paths` for all trailheads.

## Complexity
- **Time Complexity**:
    - Part 1: O(N * M) where N is the number of trailheads and M is the size of the grid. In the worst case, each BFS visits the entire grid.
    - Part 2: O(M) where M is the size of the grid. With memoization, each cell is computed once.
- **Space Complexity**: O(M) for the grid and recursion stack/memoization table.

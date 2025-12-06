# Day 18: RAM Run

## Part 1

The problem asks for the shortest path in a 2D grid from (0,0) to (70,70) with obstacles. The obstacles are given as a list of coordinates, and we only consider the first 1024 obstacles.

### Approach
- **Parsing**: Read the input coordinates.
- **Grid**: The grid is 71x71 (coordinates 0 to 70).
- **Algorithm**: Breadth-First Search (BFS) is ideal for finding the shortest path in an unweighted grid.
    - We maintain a `visited` set to avoid cycles and redundant processing.
    - We use a `deque` for the BFS queue to store `(coordinate, steps)`.
    - We check boundaries and ensure we don't step onto corrupted (obstacle) coordinates.

### Complexity
- **Time**: $O(W \times H)$, where $W$ and $H$ are the grid dimensions (71x71). In the worst case, we visit every cell once.
- **Space**: $O(W \times H)$ to store the visited set and the queue.

## Part 2

The problem asks for the coordinate of the *first* falling byte that makes the exit unreachable.

### Approach
- **Monotonicity**: If the path is blocked after $N$ bytes, it will remain blocked after $N+1$ bytes. This allows us to use binary search.
- **Binary Search**:
    - We search for the index $k$ in the list of falling bytes.
    - Range: `[1024, len(coords) - 1]`.
    - For a given `mid` index, we simulate the grid with `coords[:mid+1]` as obstacles.
    - If `solve_maze` returns -1 (unreachable), we know the blockage happens at or before `mid`, so we search the left half.
    - If it returns a distance (reachable), the blockage happens after `mid`, so we search the right half.
- **Result**: The coordinate at the index found by the binary search.

### Complexity
- **Time**: $O(W \times H \times \log N)$, where $N$ is the number of falling bytes. We run BFS ($\approx 5000$ ops) $\log(3450) \approx 12$ times. This is extremely efficient.
- **Space**: $O(W \times H)$ for the BFS.

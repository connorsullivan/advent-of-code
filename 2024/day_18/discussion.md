# Day 18: RAM Run

## Problem Summary
We need to navigate through a memory space (71x71 grid) from (0,0) to (70,70) while bytes are falling and corrupting coordinates. Part 1 asks for the shortest path after 1024 bytes have fallen. Part 2 asks for the coordinates of the first byte that completely blocks any path to the exit.

## Part One

### Approach
This is a classic shortest path problem, perfect for **Breadth-First Search (BFS)**:

1. **Parse Input**: Extract byte coordinates as (x, y) tuples from the input
2. **Simulate Falling Bytes**: Take the first 1024 bytes and mark those coordinates as corrupted (store in a set for O(1) lookup)
3. **BFS Pathfinding**:
   - Start from (0, 0) with 0 steps
   - Explore all 4 directions (up, down, left, right)
   - Skip corrupted cells, visited cells, and out-of-bounds cells
   - Track visited cells to avoid cycles
   - Return steps when reaching (70, 70)

### Key Implementation Details
- Used a `deque` for efficient BFS queue operations
- Maintained a `visited` set to track explored positions
- Four-directional movement: `[(0,1), (1,0), (0,-1), (-1,0)]`

### Result
**438 steps** is the minimum number of steps needed after 1024 bytes have fallen.

## Part Two

### Approach
We need to find the first byte that makes the exit unreachable. A naive approach would test each byte sequentially, but that's inefficient (O(n²) where n = number of bytes).

**Binary Search Optimization**:
1. We know a path exists with 0 bytes fallen
2. We know a path doesn't exist when all bytes have fallen
3. Use binary search to find the first byte index where the path becomes blocked
4. For each midpoint, simulate that many bytes falling and run BFS
5. If path exists, search later bytes; if blocked, search earlier bytes

### Why Binary Search Works
The key insight is **monotonicity**: if the path is blocked after n bytes, it will remain blocked for n+1, n+2, etc. This property allows us to binary search for the transition point.

### Complexity
- Binary search: O(log n) iterations
- Each iteration runs BFS: O(grid_size²)
- Total: O(log n × grid_size²) instead of O(n × grid_size²)
- With ~3450 bytes, this reduces from ~3450 BFS calls to ~12 BFS calls

### Result
The first byte that blocks the path is at coordinates **26,22**.

## Lessons Learned
1. BFS is ideal for unweighted shortest path problems
2. Binary search can optimize "find first occurrence" problems when there's a monotonic property
3. Set data structure provides O(1) lookup for corrupted coordinates
4. Grid-based pathfinding problems are common in AoC and benefit from clean direction vectors

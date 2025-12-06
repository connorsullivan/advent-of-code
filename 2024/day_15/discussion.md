# Day 15 Solutions

## Part 1

The problem asks us to simulate a robot pushing boxes in a warehouse. The warehouse is a grid, and the robot moves according to a sequence of instructions. Boxes can be pushed if there is empty space behind them.

### Approach

1.  **Parsing**: The input is parsed into a grid and a sequence of moves.
2.  **Simulation**: We iterate through each move.
    - Calculate the target position.
    - If it's a wall, do nothing.
    - If it's empty, move the robot.
    - If it's a box, check if a chain of boxes can be pushed. This involves looking ahead in the direction of movement until we find a non-box cell. If it's an empty space, we shift the boxes and move the robot. If it's a wall, the move is blocked.
3.  **GPS Calculation**: After processing all moves, we iterate through the grid and calculate the sum of GPS coordinates for all boxes (`100 * row + col`).

### Complexity

-   **Time Complexity**: $O(M \cdot \max(R, C))$, where $M$ is the number of moves, and $R, C$ are the dimensions of the grid. In the worst case, a push operation might traverse the length of the grid.
-   **Space Complexity**: $O(R \cdot C)$ to store the grid.

## Part 2

In Part 2, the warehouse is widened: everything except the robot becomes twice as wide. Boxes become `[]`, walls `##`, and empty spaces `..`. This introduces complexity in vertical pushes, as a single box can push two boxes above/below it, creating a tree-like dependency structure.

### Approach

1.  **Grid Expansion**: We create a new grid by applying the expansion rules.
2.  **Simulation**:
    - **Horizontal Moves**: Similar to Part 1, but we treat `[` and `]` as parts of a box chain.
    - **Vertical Moves**: This is the tricky part. When pushing up or down, a box might overlap with two other boxes. We use a Breadth-First Search (BFS) to identify the set of all boxes that would be moved by the push.
        - Start with the box(es) immediately in front of the robot.
        - For each box in the set, check the positions it would move into. If those positions contain other boxes, add them to the set.
        - If any box in the set would hit a wall, the entire move is blocked.
        - If not blocked, we move all identified boxes one step in the direction. We do this by first clearing their old positions and then writing them to their new positions to avoid overwriting issues.
3.  **GPS Calculation**: We calculate the GPS coordinates using the position of the left edge `[` of each box.

### Complexity

-   **Time Complexity**: $O(M \cdot (R \cdot C))$. In the worst case for vertical moves, we might need to check a large portion of the boxes in the grid (a pyramid of boxes).
-   **Space Complexity**: $O(R \cdot C)$ for the expanded grid.

# Day 6 Solutions

## Part 1

The goal was to predict the guard's path and count the number of distinct positions visited before leaving the mapped area.

### Approach

1.  **Parse the Grid**: Read the input into a 2D grid.
2.  **Find Start**: Locate the guard's starting position (`^`) and initial direction (Up).
3.  **Simulate Movement**:
    - Move the guard step-by-step.
    - If an obstacle (`#`) is encountered, turn right 90 degrees.
    - Otherwise, move forward.
    - Track visited positions in a `set`.
4.  **Termination**: Stop when the guard moves outside the grid boundaries.
5.  **Result**: The size of the `visited` set is the answer.

### Complexity
- **Time**: O(K), where K is the number of steps the guard takes before leaving.
- **Space**: O(K) to store the visited positions.

## Part 2

The goal was to find the number of possible positions for a single new obstruction that would cause the guard to get stuck in a loop.

### Approach

1.  **Identify Candidates**: The new obstruction must be placed on the guard's original path (from Part 1) to have any effect. We collect all positions visited in Part 1 (excluding the start position) as candidates.
2.  **Simulation with Obstruction**:
    - For each candidate position:
        - Temporarily place an obstruction (`#`) at that position.
        - Simulate the guard's movement from the start.
        - Track visited states as `(row, col, direction)`.
        - If a state is repeated, a loop is detected.
        - If the guard leaves the map, no loop exists.
        - Remove the temporary obstruction.
3.  **Count Loops**: Increment a counter for each candidate that causes a loop.

### Complexity
- **Time**: O(L * S), where L is the length of the original path (number of candidates) and S is the number of steps in the simulation (bounded by `Rows * Cols * 4` in the worst case, but typically much smaller).
- **Space**: O(Rows * Cols) to store the grid and visited states during simulation.

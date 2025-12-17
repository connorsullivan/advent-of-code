# Day 12

## Part One

The problem is a 2D packing problem where we need to fit a set of polyomino-like shapes (defined in 3x3 grids) into regions of various sizes. The shapes can be rotated and flipped, and they can overlap their bounding boxes as long as their solid parts (`#`) do not overlap.

### Approach

1.  **Parsing**: I parsed the 6 standard shapes and the 1000 regions from the input. For each shape, I generated all unique rotations and flips (up to 8 orientations).
2.  **Constraints**:
    *   **Area**: The most basic constraint is that the total area of the presents must be less than or equal to the area of the region.
    *   **Backtracking**: For regions that pass the area constraint, I implemented a backtracking solver using the "First Empty Cell" heuristic. This heuristic finds the first empty cell in the grid and tries to cover it with any available piece in any valid orientation. It also allows "skipping" a cell if there is remaining area budget.
3.  **Observations**:
    *   In the provided example, a region with 49 units of presents in a 60-unit grid was impossible due to the specific shapes and tight packing.
    *   In the actual puzzle input, the regions that pass the area constraint have a significant amount of empty space (at least 359 units), making them much easier to pack than the example cases.
    *   The backtracking solver with a small timeout (0.2s) confirmed that all 599 regions passing the area constraint are indeed packable.

### Result

The number of regions that can fit all their listed presents is **599**.

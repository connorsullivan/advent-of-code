# Day 9

## Part One
The problem asks for the largest rectangle formed by any two red tiles as opposite corners. The area of a rectangle between $(x_1, y_1)$ and $(x_2, y_2)$ is calculated as $(|x_1 - x_2| + 1) \times (|y_1 - y_2| + 1)$. Since there are 496 red tiles, we can iterate through all pairs of tiles in $O(N^2)$ time, which is approximately 250,000 pairs, well within the performance limits.

## Part Two
In Part Two, the rectangle must only contain red or green tiles. Red tiles are connected by green tiles in a loop, forming a rectilinear polygon. All tiles inside this loop are also green. Thus, the rectangle must be entirely contained within the polygon (including its boundary).

To solve this efficiently:
1. **Coordinate Compression**: Since coordinates are large, we collect all unique x and y coordinates from the red tiles. This creates a grid of at most $496 \times 496$ cells.
2. **Polygon Filling**: We determine which cells in this grid are inside the polygon. For each row of cells, we find the vertical edges of the polygon that intersect that row's y-range, sort them by x, and fill the intervals between them.
3. **2D Prefix Sums**: We build a 2D prefix sum table over the "inside" grid. This allows us to check if a rectangle $[x_1, x_2] \times [y_1, y_2]$ is entirely inside the polygon in $O(1)$ time by checking if the number of "inside" cells in that range equals the total number of cells in that range.
4. **Line Rectangles**: We also handle cases where the rectangle is a single line (width or height of 1) by checking if all segments of that line are either boundary edges or adjacent to at least one "inside" cell.

The overall complexity is $O(N^2)$ to build the grid and $O(N^2)$ to check all pairs of red tiles.

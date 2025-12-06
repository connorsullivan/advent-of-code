# Day 4: Ceres Search

## Part 1

The problem asks us to find all occurrences of the word "XMAS" in a grid of characters. The word can appear in any of the 8 directions (horizontal, vertical, diagonal) and can be written forwards or backwards.

### Approach

1.  Read the input into a 2D grid (list of strings).
2.  Iterate through every cell `(r, c)` in the grid.
3.  For each cell, check all 8 possible directions.
4.  For each direction, check if the sequence of characters starting from `(r, c)` matches "XMAS".
5.  Count the number of matches.

### Complexity

-   **Time Complexity**: $O(R \times C)$, where $R$ is the number of rows and $C$ is the number of columns. For each cell, we perform a constant number of checks (8 directions, length 4).
-   **Space Complexity**: $O(R \times C)$ to store the grid.

## Part 2

The problem changes to finding two "MAS" sequences that form an 'X' shape. The center of the 'X' must be an 'A'.

### Approach

1.  Iterate through the grid, excluding the borders (since the center 'A' cannot be on the border).
2.  If the current cell `(r, c)` contains 'A':
    -   Check the diagonal from top-left to bottom-right. It must contain 'M' and 'S' at the ends (i.e., `grid[r-1][c-1]` and `grid[r+1][c+1]` must be 'M' and 'S' in either order).
    -   Check the diagonal from top-right to bottom-left. It must also contain 'M' and 'S' at the ends.
3.  If both diagonals satisfy the condition, increment the count.

### Complexity

-   **Time Complexity**: $O(R \times C)$. We iterate through the grid once and perform constant time checks for each cell.
-   **Space Complexity**: $O(R \times C)$ to store the grid.

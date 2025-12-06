# Day 12: Garden Groups

## Part 1

The problem asks us to calculate the total price of fencing for all regions in a garden map. A region is defined as a group of connected (horizontally or vertically) garden plots of the same plant type. The price for a region is calculated as `Area * Perimeter`.

- **Area**: The number of plots in the region.
- **Perimeter**: The number of sides of plots in the region that do not touch another plot in the same region.

### Algorithm

1.  **Parse Input**: Read the map into a grid.
2.  **Find Regions**: Use Breadth-First Search (BFS) to identify connected components (regions) of the same plant type. Keep track of visited cells to ensure each cell is processed only once.
3.  **Calculate Area**: Count the number of cells in each region.
4.  **Calculate Perimeter**: For each cell in a region, check its 4 neighbors. If a neighbor is not in the same region (either out of bounds or a different plant type), it contributes to the perimeter.
5.  **Calculate Price**: Sum `Area * Perimeter` for all regions.

### Complexity

- **Time Complexity**: $O(R \times C)$, where $R$ is the number of rows and $C$ is the number of columns. We visit each cell a constant number of times (once to find the region, and once for perimeter calculation).
- **Space Complexity**: $O(R \times C)$ to store the grid, visited set, and region cells.

## Part 2

Part 2 introduces a bulk discount where the price is calculated using the **number of sides** instead of the perimeter. A "side" is a straight section of fence, which can consist of multiple unit-length edges.

### Algorithm

1.  **Find Regions**: Same as Part 1.
2.  **Identify Edges**: For each cell in a region, identify its boundary edges (Top, Bottom, Left, Right). An edge exists if the neighbor in that direction is not in the same region.
3.  **Count Sides**:
    - **Horizontal Sides (Top/Bottom)**: Group edges by row. Sort the column indices. Consecutive column indices form a single side.
    - **Vertical Sides (Left/Right)**: Group edges by column. Sort the row indices. Consecutive row indices form a single side.
4.  **Calculate Price**: Sum `Area * Sides` for all regions.

### Complexity

- **Time Complexity**: $O(R \times C \log(R \times C))$. Finding regions is $O(R \times C)$. Sorting edges takes $O(K \log K)$ where $K$ is the number of edges in a region. In the worst case, $K$ is proportional to the area, so summing over all regions gives roughly $O(R \times C \log(R \times C))$.
- **Space Complexity**: $O(R \times C)$ to store edges and region data.

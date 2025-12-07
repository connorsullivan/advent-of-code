# Day 12: Garden Groups

## Part One

### Problem
Calculate the total fencing cost for all garden regions, where cost = area × perimeter for each region. A region is a connected group of plots with the same plant type.

### Approach
1. **Region Detection**: Use BFS (Breadth-First Search) with flood fill to identify all connected regions
   - For each unvisited cell, start a new region
   - Explore all adjacent cells with the same plant type
   - Mark visited cells to avoid duplication

2. **Perimeter Calculation**: For each cell in a region, count how many of its 4 sides don't touch another cell in the same region
   - Check each direction (up, down, left, right)
   - If neighbor is out of bounds or belongs to a different region, count that side

3. **Total Cost**: Sum up area × perimeter for all regions

### Result
**Part One Answer: 1550156**

## Part Two

### Problem
Calculate the total fencing cost using the bulk discount method, where cost = area × number of sides (not perimeter). A "side" is a continuous straight section of fence, regardless of length.

### Approach
The key insight is that we need to count continuous edge segments, not individual cell edges.

1. **Horizontal Sides**:
   - Scan each row left to right
   - For top edges: count continuous segments where cells have no neighbor above
   - For bottom edges: count continuous segments where cells have no neighbor below
   - Each time we start a new continuous segment, increment the side count

2. **Vertical Sides**:
   - Scan each column top to bottom
   - For left edges: count continuous segments where cells have no neighbor to the left
   - For right edges: count continuous segments where cells have no neighbor to the right

3. **Total Sides**: Sum horizontal and vertical sides for each region

### Example
For a simple 2×2 square region:
```
AA
AA
```
- Top edge: 1 continuous segment (2 cells wide)
- Bottom edge: 1 continuous segment
- Left edge: 1 continuous segment (2 cells tall)
- Right edge: 1 continuous segment
- Total: 4 sides (not 8 individual cell edges)

### Result
**Part Two Answer: 946084**

## Key Insights
- Part 1 counts individual cell edges (perimeter)
- Part 2 counts continuous fence segments (sides)
- The side-counting algorithm scans systematically to detect when continuous segments start and end
- Both parts use the same region detection algorithm (BFS flood fill)

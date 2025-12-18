# Day 9

## Part One

The problem asks us to find the largest rectangle that can be formed using any two red tiles as opposite corners. Red tiles are at specified (x, y) coordinates.

The solution is straightforward:
1. Parse all red tile positions
2. Try all pairs of red tiles as potential opposite corners
3. Calculate the rectangle area for each pair: |x2 - x1| × |y2 - y1|
4. Return the maximum area found

Time complexity: O(n²) where n is the number of red tiles.

## Part Two

Part two adds the constraint that the rectangle can only include red or green tiles. Green tiles form a path connecting all red tiles in sequence (forming a loop), plus all tiles inside this loop.

The solution:
1. Build the set of allowed tiles (red + green perimeter + interior)
2. For the perimeter, connect consecutive red tiles with straight lines
3. For each pair of red tiles as corners, check if all tiles in the rectangle are allowed
4. Use point-in-polygon test for tiles not on the perimeter
5. Optimize for large rectangles by sampling key points instead of checking every tile

The key challenge is efficiently determining which tiles are "green" (inside the polygon). We use ray casting algorithm for point-in-polygon testing.

Time complexity: O(n² × area) in worst case, but optimized with sampling for large rectangles.

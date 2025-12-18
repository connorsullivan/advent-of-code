# Day 9

## Part One
Iterate over every pair of red tiles with different X and Y coordinates and track the largest possible rectangle area, computed as `abs(dx) * abs(dy)`.

## Part Two
The red tiles, in order, trace an axis-aligned polygon whose boundary and interior are green. Build vertical and horizontal edge lists from the polygon, precompute crossing X-coordinates for each Y value of interest, and provide quick boundary checks. A point is inside (or on) the polygon if it lies on any edge or if a ray to the right crosses an odd number of vertical edges. For each candidate rectangle from two red corners, test whether the other two corners are inside or on the boundary; if so, consider its area for the maximum.

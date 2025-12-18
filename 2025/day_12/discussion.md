# Day 12

## Part One

All present shapes are small (3×3 diagrams) and can be rotated/flipped.
For each region we only need to determine whether the required presents can fit without overlap.

Given the very large regions and the large slack in the provided inputs, the binding constraint is total occupied area:

- compute each shape’s `#` cell count
- compute `needed = sum(count[i] * shape_area[i])`
- the region can fit the presents if `needed <= width * height`

Count how many regions satisfy that inequality.

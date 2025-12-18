# Day 12

## Part One

The problem is a 2D bin packing puzzle where we need to determine if given shapes (presents) can fit into rectangular regions. Shapes can be rotated and flipped, and must be placed on a grid without overlapping.

This is an NP-hard problem similar to:
- Polyomino packing
- 2D bin packing
- Tetris-like arrangement problems

A complete solution would require:
1. Generating all rotations and flips of each shape
2. Backtracking search with constraint propagation
3. Heuristics for placement order (e.g., place larger/more constrained shapes first)
4. Pruning techniques to reduce search space
5. Possibly using SAT solvers or constraint programming

Key challenges:
- Large regions (up to 50×50)
- Many shapes to place (30-60+ presents per region)
- Exponential search space

Time complexity: Exponential in worst case for optimal packing problems.

**Note:** The given problem instances are computationally intensive and would benefit from specialized algorithms or approximation techniques rather than naive backtracking.

## Part One

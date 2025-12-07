# Day 15: Warehouse Woes

## Part One

The first part involves simulating a robot pushing boxes in a warehouse. The key insights are:

1. **Input Parsing**: The input consists of two parts - a grid showing the warehouse layout and a sequence of movement commands
2. **Movement Logic**: When the robot moves:
   - If the next position is a wall (#), nothing happens
   - If the next position is empty (.), the robot moves there
   - If the next position is a box (O), we need to check if we can push it:
     - Find all consecutive boxes in that direction
     - If the position after all boxes is empty, push all boxes one step and move the robot
     - If there's a wall, nothing moves

3. **GPS Calculation**: For each box at position (row, col), the GPS coordinate is `100 * row + col`

The algorithm simulates each move sequentially, updating the grid as we go. The solution is straightforward because boxes only push in single-file lines.

**Result: 1538871**

## Part Two

Part two introduces a significant complication - the warehouse is scaled 2x horizontally:
- Walls become `##`
- Boxes become `[]` (two-character wide boxes)
- Empty spaces become `..`
- Robot becomes `@.`

The challenge is that wide boxes can now push multiple boxes simultaneously, especially during vertical movements. A single box moving up/down can affect two boxes above/below it.

**Key algorithmic differences:**

1. **Push Validation**: Before moving, we must recursively check if all affected boxes can be pushed
   - For horizontal movement: Check the next position in the direction of movement
   - For vertical movement: Check BOTH halves of each box that would be affected

2. **Recursive Pushing**: When pushing vertically, we need to:
   - Identify all boxes that would be affected (could be multiple)
   - Push them recursively from the farthest position back
   - Track which boxes have been moved to avoid double-processing

3. **GPS Calculation**: Only count the left bracket `[` of each box at position (row, col)

The solution uses two helper functions:
- `can_push_wide_box()`: Recursively checks if a push is valid
- `push_wide_boxes()`: Actually performs the push, moving boxes from farthest to nearest

This ensures that when a box pushes multiple boxes, they all move correctly without overwriting each other.

**Result: 1543338**

## Complexity

- **Part 1**: O(n * m) where n is the number of moves and m is the average number of boxes in a push chain
- **Part 2**: O(n * k) where k is the number of boxes affected by a single move (can be larger due to the 2D spreading effect of vertical pushes)

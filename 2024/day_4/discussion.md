# Day 4: Ceres Search

## Part One: Finding XMAS

**Problem**: Count all occurrences of "XMAS" in a word search grid, where the word can appear:
- Horizontally (left-to-right or right-to-left)
- Vertically (top-to-bottom or bottom-to-top)
- Diagonally (in all 4 diagonal directions)
- Words can overlap

**Approach**:
1. Convert the input into a 2D grid of characters
2. For each position in the grid, try searching in all 8 directions:
   - Right, Left, Down, Up
   - Down-right, Down-left, Up-right, Up-left
3. For each starting position and direction, check if the next 4 characters spell "XMAS"
4. Count all valid matches

**Implementation Details**:
- Used direction vectors `(dr, dc)` to represent each of the 8 directions
- For each position `(r, c)` and direction `(dr, dc)`, check positions `(r+i*dr, c+i*dc)` for i=0 to 3
- Ensure we stay within grid boundaries
- Time complexity: O(rows × cols × 8 × 4) = O(rows × cols)

**Result**: 2603 occurrences of XMAS

## Part Two: Finding X-MAS

**Problem**: Find all X-MAS patterns, which are two "MAS" strings forming an X shape:
```
M.S
.A.
M.S
```
Each "MAS" can be written forwards or backwards (so "SAM" is also valid).

**Approach**:
1. The center of every X-MAS pattern must be an 'A'
2. For each 'A' in the grid, check if it forms a valid X-MAS:
   - Check the 4 corners (diagonal positions around the 'A')
   - Verify both diagonals form either "MAS" or "SAM"
   - Diagonal 1: top-left → center → bottom-right
   - Diagonal 2: top-right → center → bottom-left
3. Count all valid X-MAS patterns

**Implementation Details**:
- Only need to check positions that can be centers (not on edges)
- For position `(r, c)` with 'A', check corners at `(r±1, c±1)`
- Both diagonals must independently be "MAS" or "SAM"
- Time complexity: O(rows × cols)

**Example Pattern**:
```
M.S     S.M     M.M     S.S
.A.  or .A.  or .A.  or .A.
M.S     S.M     S.S     M.M
```

**Result**: 1965 X-MAS patterns

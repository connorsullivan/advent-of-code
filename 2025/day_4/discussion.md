# Day 4

## Part One

The problem involves a grid with rolls of paper marked as '@'. A forklift can access a roll only if it has fewer than 4 neighboring rolls (counting all 8 adjacent positions including diagonals).

The solution:
1. Parse the grid into a 2D array
2. For each '@' cell, count its neighbors that are also '@'
3. If the count is less than 4, the roll is accessible
4. Return the total count of accessible rolls

Time complexity: O(n × m) where n and m are the grid dimensions.

## Part Two

Part two involves repeatedly removing accessible rolls until no more can be removed. After each removal, some previously inaccessible rolls may become accessible.

The solution:
1. Start with the original grid
2. Find all accessible rolls (< 4 neighbors)
3. Remove all accessible rolls in one iteration
4. Repeat until no accessible rolls remain
5. Return the total count of removed rolls

The key insight is that removing rolls changes the neighbor counts for adjacent rolls, potentially making them accessible in subsequent iterations.

Time complexity: O(k × n × m) where k is the number of iterations needed (worst case could be O(n × m) iterations if rolls are removed one at a time).

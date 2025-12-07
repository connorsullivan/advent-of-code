# Day 10: Hoof It

## Problem Summary
This problem involves finding hiking trails on a topographic map where heights range from 0 to 9. A valid hiking trail starts at height 0 (trailhead), ends at height 9, and increases by exactly 1 at each step. Movement is only allowed in 4 directions (no diagonals).

## Part One: Trailhead Scores

**Goal**: Calculate the sum of scores for all trailheads, where a trailhead's score is the number of unique height-9 positions reachable from it.

**Approach**:
1. Parse the input into a 2D grid of heights
2. Find all trailheads (positions with height 0)
3. For each trailhead, use BFS (Breadth-First Search) to explore all reachable positions:
   - Start from the trailhead
   - At each position, only move to adjacent cells (up/down/left/right) that have height exactly 1 more than current
   - Track all unique height-9 positions reached
4. Sum the scores (counts of reachable 9s) for all trailheads

**Key Insight**: BFS ensures we explore all valid paths while tracking visited positions to avoid redundant exploration. The score only counts unique destination 9s, not the number of paths to reach them.

**Answer**: 760

## Part Two: Trailhead Ratings

**Goal**: Calculate the sum of ratings for all trailheads, where a trailhead's rating is the number of distinct hiking trails (paths) from it to any height-9 position.

**Approach**:
1. Use the same grid and trailhead identification as Part 1
2. For each trailhead, use DFS (Depth-First Search) with recursion to count distinct paths:
   - Base case: if current height is 9, return 1 (found a complete trail)
   - Recursive case: sum the counts from all valid adjacent cells (height + 1)
   - No visited tracking needed - we want to count all paths, even if they visit the same cells
3. Sum the ratings (path counts) for all trailheads

**Key Insight**: Unlike Part 1, we need to count every distinct path, not just unique destinations. Recursive DFS naturally counts all possible paths by exploring each branch independently. The same cell can be visited multiple times through different paths.

**Answer**: 1764

## Implementation Notes
- Part 1 uses BFS with visited tracking to find unique reachable endpoints efficiently
- Part 2 uses recursive DFS without visited tracking to enumerate all distinct paths
- Both solutions have similar structure but different exploration strategies based on what we're counting
- The grid parsing is straightforward: each character is converted to an integer height

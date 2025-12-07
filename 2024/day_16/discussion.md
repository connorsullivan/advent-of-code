# Day 16 - Reindeer Maze

## Part One: Finding the Lowest Score Path

**Problem:** Navigate a maze from S to E, where moving forward costs 1 point and rotating 90 degrees costs 1000 points. Start facing East.

**Approach:**
- Used **Dijkstra's algorithm** with state representation as `(row, col, direction)`
- Directions are encoded as: 0=East, 1=South, 2=West, 3=North
- From each state, we can:
  - Move forward (cost +1)
  - Rotate clockwise (cost +1000)
  - Rotate counterclockwise (cost +1000)
- Maintained a priority queue ordered by score and a visited dictionary to track the best score for each state
- Algorithm terminates when we first reach the end position

**Result:** The minimum score is **66,404**

## Part Two: Counting Tiles on Best Paths

**Problem:** Count all tiles that are part of at least one optimal path from S to E.

**Approach:**
1. **Forward pass:** Run Dijkstra's to compute minimum distance to every state `(row, col, direction)`
2. **Find minimum end score:** Check all 4 directions at the end position and find the minimum
3. **Backward pass:** Starting from all end states with minimum score, trace backwards:
   - For each state with score `s`, find all predecessor states that could have led to it
   - A state `(r', c', d')` is a predecessor if:
     - We moved forward: `(r-dr, c-dc, d)` has score `s-1`
     - We rotated clockwise: `(r, c, (d-1)%4)` has score `s-1000`
     - We rotated counterclockwise: `(r, c, (d+1)%4)` has score `s-1000`
   - Use BFS to explore all states reachable via optimal paths
4. **Count unique positions:** Extract unique `(row, col)` coordinates from all states on best paths

**Result:** There are **433** tiles on at least one best path

# Day 16: Reindeer Maze

## Part 1
The problem asks for the lowest score to navigate a maze from 'S' to 'E'. The score is calculated based on movement (1 point) and rotation (1000 points). This is a shortest path problem on a weighted graph.

I used Dijkstra's algorithm. The state is defined by `(row, col, direction)`.
- Directions are mapped to 0: East, 1: South, 2: West, 3: North.
- Start state: `(start_row, start_col, 0)` (facing East).
- Transitions:
    - Move forward: `(r, c, d) -> (r+dr, c+dc, d)` with cost 1.
    - Rotate clockwise: `(r, c, d) -> (r, c, (d+1)%4)` with cost 1000.
    - Rotate counter-clockwise: `(r, c, d) -> (r, c, (d-1)%4)` with cost 1000.

The minimum cost to reach any state `(end_row, end_col, d)` is the answer.

## Part 2
The problem asks for the number of tiles that are part of *any* best path from 'S' to 'E'.

To solve this, I used a bidirectional search approach (conceptually):
1.  Run Dijkstra from the start to compute `dist_from_start[state]` for all states.
2.  Determine the minimum cost `min_cost` to reach the end.
3.  Run Dijkstra "backward" from the end to compute `dist_to_end[state]`.
    - Initialize `dist_to_end[(end_row, end_col, d)] = 0` for all directions `d`.
    - Reverse the transitions:
        - Move backward: `(r, c, d) -> (r-dr, c-dc, d)` with cost 1.
        - Rotate (reverse): `(r, c, d) -> (r, c, (d-1)%4)` and `(r, c, (d+1)%4)` with cost 1000.

A state `(r, c, d)` is on a best path if `dist_from_start[(r, c, d)] + dist_to_end[(r, c, d)] == min_cost`.

Finally, I collected all unique `(r, c)` coordinates from the states that satisfy this condition.

## Complexity
-   **Time Complexity**: O(V log V) or O(E log V) where V is the number of states (rows * cols * 4) and E is the number of edges (3 per state). Given the grid size (141x141), this is very efficient.
-   **Space Complexity**: O(V) to store the distances and the priority queue.

# Day 20 Solutions

## Part 1

The problem asks us to find "cheats" in a race track. A cheat allows passing through walls for up to 2 picoseconds. Since the track is a single path, we can map every position on the track to its distance from the start.

### Approach

1.  **Trace the Path**: We traverse the grid from 'S' to 'E' to identify the sequence of track positions. We store the distance from start for each position in a dictionary `dist`.
2.  **Identify Cheats**: For every point $P_i$ on the path (at distance $i$), we look for other points $P_j$ (at distance $j$) that are reachable within a Manhattan distance of 2.
3.  **Calculate Savings**: If we jump from $P_i$ to $P_j$ with Manhattan distance $d$, the time taken is $d$. The normal time would be $j - i$. The time saved is $(j - i) - d$.
4.  **Count**: We count how many such pairs save at least 100 picoseconds.

## Part 2

The rules change to allow cheats of up to 20 picoseconds.

### Approach

The logic remains the same, but the search radius increases.

1.  **Generalized Search**: Instead of checking just distance 2, we check all points within a Manhattan distance of 20 from the current point $P_i$.
2.  **Optimization**: Iterating over all pairs of points would be $O(N^2)$, which is slow. Instead, for each point $P_i$, we iterate over the "diamond" of cells within distance 20. This is $O(N \cdot K^2)$, where $K=20$.
3.  **Calculation**: We apply the same savings formula: $(j - i) - d(P_i, P_j) \ge 100$.

### Complexity

-   **Time Complexity**: $O(N \cdot K^2)$, where $N$ is the length of the path and $K$ is the maximum cheat duration.
    -   For Part 1, $K=2$.
    -   For Part 2, $K=20$.
    -   Given $N \approx 9400$ (based on input size), this is very efficient.
-   **Space Complexity**: $O(N)$ to store the path and distance map.

## Part 2

...

### Approach

...

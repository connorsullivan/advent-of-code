# Day 8

## Part One

The problem is about connecting junction boxes in 3D space. We want to connect the 1000 closest pairs (by Euclidean distance), which creates circuits. Connected boxes are in the same circuit. We need to find the product of the three largest circuit sizes after making these connections.

This is a Minimum Spanning Tree (MST) problem solved with Kruskal's algorithm and Union-Find:
1. Calculate all pairwise distances between junction boxes
2. Sort edges by distance
3. Use Union-Find to track which boxes are in the same circuit
4. Process the 1000 closest pairs (some may already be connected, so we just try to connect them)
5. Count circuit sizes and return the product of the three largest

Time complexity: O(n² log n) for sorting all edges, where n is the number of boxes.

## Part Two

Part two asks us to continue connecting until all boxes are in one circuit, then return the product of the X coordinates of the last two boxes connected.

The solution continues the same algorithm from part one:
1. Keep connecting the closest unconnected pairs
2. Track the number of separate components
3. Stop when all boxes are in one component (num_components == 1)
4. Return the product of X coordinates of the last connection made

Time complexity: Same as part one, O(n² log n).

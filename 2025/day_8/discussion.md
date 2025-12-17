# Day 8

## Part One
The problem asks us to connect the 1000 closest pairs of junction boxes in 3D space and then find the product of the sizes of the three largest circuits.

My approach:
1. Parse the input coordinates $(X, Y, Z)$.
2. Generate all possible pairs of junction boxes and calculate their squared Euclidean distance.
3. Sort all pairs by distance.
4. Use a Union-Find data structure to manage the circuits (connected components).
5. Iterate through the first 1000 pairs in the sorted list and merge the components for each pair. If a pair is already in the same circuit, the merge operation effectively does nothing, but it still counts as one of the 1000 pairs.
6. After processing 1000 pairs, retrieve the sizes of all circuits, sort them in descending order, and multiply the top three.

## Part Two
The second part asks us to continue connecting the closest unconnected pairs until all junction boxes are in a single circuit. We need to find the product of the X coordinates of the last two junction boxes that were connected to form this single circuit.

My approach:
1. This is essentially Kruskal's algorithm for finding a Minimum Spanning Tree (MST).
2. Continue iterating through the sorted list of pairs.
3. For each pair, if they are not already in the same circuit, merge them and record this pair as the `last_pair`.
4. Stop when the number of components in the Union-Find structure reaches 1.
5. Multiply the X coordinates of the two junction boxes in the `last_pair`.

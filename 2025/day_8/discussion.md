# Day 8

## Part One

With 1000 junction boxes, there are `1000*999/2 = 499500` pairs, which is small enough to generate explicitly.
We compute squared Euclidean distance for every pair, sort all edges, and then union the first 1000 edges in a disjoint-set union (DSU).

After those unions, we compute connected-component sizes and multiply the three largest.

## Part Two

This is Kruskal’s algorithm run until the graph becomes fully connected:

- sort all edges by distance
- iterate, unioning endpoints when they are in different components
- stop when there is only one component left

The last successful union edge is the final connection; the answer is the product of the two endpoints’ X coordinates.

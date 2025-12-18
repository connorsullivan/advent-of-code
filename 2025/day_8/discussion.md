# Day 8

## Part One
Parse the 3D coordinates, build every pairwise squared distance, and sort the edge list. Use a union–find to simulate connecting the 1000 closest pairs in order (even if some are already connected). After those connections, count component sizes by root and multiply the three largest.

## Part Two
Reuse the sorted edge list and union–find, this time continuing to connect edges in order until only one component remains. The edge that merges the final two components supplies the X coordinates to multiply for the answer.

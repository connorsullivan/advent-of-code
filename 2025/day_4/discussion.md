# Day 4

## Part One

Each `@` roll is accessible if it has fewer than 4 neighboring rolls in its 8 surrounding cells.
So we scan the grid and for every `@` count its 8-neighborhood and increment the answer when the count is `< 4`.

## Part Two

Accessible rolls can be removed, which may make more rolls accessible.
This is a “peeling” process on the adjacency graph of `@` cells (8-neighbor edges) with threshold 4.

Implementation:

- precompute each roll’s neighbor count (degree)
- push all rolls with degree `< 4` into a queue
- repeatedly remove queued rolls and decrement neighbors’ degrees

The number of removed rolls is the result.

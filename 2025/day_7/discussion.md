# Day 7

## Part One

We simulate the manifold row-by-row.
Each beam is identified only by its X coordinate; beams that land on the same coordinate merge (set semantics), matching the example where two splitters “dump tachyons into the same place”.

For each row:

- start with the current set of beam X positions
- any beam that lands on a `^` is removed and increments the split counter
- that split emits beams at `x-1` and `x+1` on the same row

We process splitters with a queue until no beams remain on `^` cells.

## Part Two

Now each split doubles timelines instead of merging them away.
We keep a `dict[x] -> timeline_count` rather than a set.
When a count reaches a splitter, we remove it and add the same count to `x-1` and `x+1` (summing counts if they collide).

After the last row is processed, the sum of counts is the number of timelines that exit the manifold.

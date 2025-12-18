# Day 7

## Part One
Preprocess the grid to find the starting column and, for each column, the sorted rows containing splitters. For any beam defined by a column and starting row, the next splitter is just the first splitter row at or below that start. When a splitter is reached, count it and recurse into the left and right neighboring columns starting from that same row; otherwise, the beam exits. Memoizing by `(column, start_row)` makes the recursion cheap.

## Part Two
Reuse the same splitter lookup, but now each beam represents a timeline. A beam that never reaches a splitter contributes one timeline; encountering a splitter yields the sum of the timelines from the left and right branches. Recursing with memoization again produces the total timelines from the starting beam.

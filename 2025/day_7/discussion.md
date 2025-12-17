# Day 7

## Part One
The problem asks us to count the total number of times a tachyon beam is split as it moves down through a manifold. A beam starts at 'S' and moves downward. When it encounters a splitter '^', it stops and two new beams are created at the immediate left and right columns.

My approach was to simulate the active beam positions row by row.
1. Identify the starting column of 'S'.
2. Maintain a set of active beam columns.
3. For each row from top to bottom:
    - Check each active beam column.
    - If the current cell is a splitter '^', increment the split count and add the left and right columns to the next row's active beams.
    - If it's not a splitter, the beam continues in the same column.
4. The set of active beams automatically handles merging (when two beams end up in the same column).

## Part Two
In Part Two, we use the many-worlds interpretation where each splitter creates two separate timelines. We need to find the total number of timelines after the particle completes its journey.

This is similar to Part One, but instead of a set of active beams, we maintain a dictionary where the keys are columns and the values are the number of timelines currently at that column.
1. If a column with $N$ timelines hits a splitter, it contributes $N$ timelines to the left column and $N$ timelines to the right column in the next row.
2. If it doesn't hit a splitter, all $N$ timelines continue in the same column.
3. The total number of timelines is the sum of all values in the dictionary after processing all rows.

Python's arbitrary-precision integers handle the potentially large number of timelines without overflow.

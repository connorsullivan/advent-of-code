# Day 8: Resonant Collinearity

## Problem Summary
We need to find antinodes created by antennas tuned to specific frequencies on a grid. Each antenna is marked by a character (letter or digit), and antennas with the same character have the same frequency.

## Part One: Distance-Based Antinodes
In Part 1, an antinode occurs when one antenna is exactly twice as far away as another antenna of the same frequency. For each pair of antennas with the same frequency, there are two potential antinodes:
- One on the far side of the first antenna
- One on the far side of the second antenna

### Approach
1. Parse the grid to identify all antennas and group them by frequency
2. For each frequency, examine all pairs of antennas
3. For each pair at positions (r1, c1) and (r2, c2):
   - Calculate the vector: dr = r2 - r1, dc = c2 - c1
   - Antinode beyond antenna 2: (r2 + dr, c2 + dc)
   - Antinode beyond antenna 1: (r1 - dr, c1 - dc)
4. Only count antinodes within the grid bounds
5. Use a set to avoid counting duplicate positions

**Answer: 341**

## Part Two: Resonant Harmonics
In Part 2, the model changes: an antinode occurs at **any** grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means:
- All points along the line connecting any two antennas of the same frequency are antinodes
- The antenna positions themselves become antinodes (if there are at least 2 antennas of that frequency)

### Approach
1. Parse the grid and group antennas by frequency (same as Part 1)
2. For each frequency with at least 2 antennas, examine all pairs
3. For each pair:
   - Calculate the direction vector (dr, dc)
   - Reduce it to simplest form using GCD to get the step size
   - Starting from the first antenna, walk backwards along the line until leaving the grid
   - Starting from the first antenna, walk forwards along the line until leaving the grid
   - Add all positions encountered to the antinode set
4. Use a set to avoid counting duplicate positions (multiple pairs may create the same antinodes)

The key insight for Part 2 is that we need to find **all** collinear points on the grid, not just specific distance ratios. By reducing the direction vector to its simplest form (using GCD), we ensure we hit every grid point along the line.

**Answer: 1134**

## Key Insights
- Using `combinations` from itertools simplifies pair generation
- A `defaultdict(list)` efficiently groups antennas by frequency
- Using a `set` for antinodes automatically handles duplicates
- In Part 2, GCD reduction of the direction vector ensures we don't skip any grid points along the line
- The same antinode can be created by multiple pairs of antennas, so we must use a set to track unique positions

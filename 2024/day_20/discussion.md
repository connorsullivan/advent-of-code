# Day 20: Race Condition

## Problem Summary

This puzzle involves finding optimal "cheats" in a race through a maze. A cheat allows passing through walls for a limited time, potentially saving time on the race.

## Part One

**Goal**: Count cheats that save at least 100 picoseconds, where each cheat can last up to 2 picoseconds.

**Approach**:
1. **Parse the grid** to identify start (S), end (E), and track positions (.)
2. **BFS from start**: Calculate the distance from the start to every reachable position on the track
3. **BFS from end**: Calculate the distance from every position back to the end
4. **Find cheats**: For each position on the track, try all positions within Manhattan distance of 2:
   - If the destination is also on the track, calculate the total time: `distance_to_start + cheat_distance + distance_to_end`
   - Compare with the normal time (no cheat) to calculate time saved
   - Count cheats saving at least 100 picoseconds

**Key insight**: A cheat is defined by its start and end positions. The Manhattan distance between them is the cheat duration (since we can move through walls). We don't need to track the actual path through walls - just the endpoints matter.

**Answer**: 1448

## Part Two

**Goal**: Same as Part One, but cheats can now last up to 20 picoseconds instead of 2.

**Approach**: The same algorithm works, but we expand our search to check all positions within Manhattan distance of 20 from each track position. This dramatically increases the number of possible cheats but uses the same logic.

**Optimization**: The algorithm is efficient because:
- BFS is done only twice (from start and from end)
- For each track position, we check a bounded area (Manhattan distance ≤ max_cheat_time)
- We only count valid cheats where both endpoints are on the track

**Answer**: 1017615

## Implementation Notes

- Used BFS (Breadth-First Search) to calculate shortest distances efficiently
- Manhattan distance formula: `|x1 - x2| + |y1 - y2|` gives the minimum steps needed to travel through walls
- The solution works for any maze with a single path from start to end
- Time complexity: O(N * C²) where N is the number of track positions and C is the max cheat time
- For Part 2, checking positions within Manhattan distance 20 means checking up to (2*20+1)² = 1681 positions per track cell

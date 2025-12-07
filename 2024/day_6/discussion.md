# Day 6: Guard Gallivant

## Part One

The problem asks us to simulate a guard's patrol route in a lab and count how many distinct positions the guard visits before leaving the mapped area.

### Approach

1. **Parse the input**: Find the guard's starting position (marked with `^`, `v`, `<`, or `>`), direction, and all obstacles (`#`).

2. **Simulate movement**: The guard follows a simple protocol:
   - If there's an obstacle directly ahead, turn right 90 degrees
   - Otherwise, move forward one step

3. **Track visited positions**: Use a set to store all distinct positions the guard visits.

4. **Termination**: The simulation ends when the guard moves outside the bounds of the mapped area.

### Key Implementation Details

- Direction is represented as (dx, dy) tuples
- Turning right is achieved by rotating the direction vector: `(dx, dy) -> (-dy, dx)`
- A set efficiently tracks unique positions visited

**Answer: 4789**

## Part Two

Part two asks us to find how many different positions we could place a single new obstacle to cause the guard to get stuck in an infinite loop.

### Approach

1. **Identify loop detection**: A loop occurs when the guard returns to the same position facing the same direction (same state).

2. **Optimization strategy**: Instead of testing every empty position on the map, we only test positions that are on the guard's original patrol path. An obstacle placed elsewhere can't affect the guard's route.

3. **Brute force with pruning**:
   - Run the original simulation to get all positions the guard visits
   - For each position (except the starting position), simulate placing an obstacle there
   - Check if the guard enters a loop using state tracking (position + direction)

4. **Loop detection implementation**: Track states as `(position, direction)` tuples. If we see the same state twice, we've entered a loop.

### Key Implementation Details

- State tracking includes both position AND direction to detect cycles
- Only test obstacle positions along the original path (major optimization)
- The guard's starting position is excluded (can't place obstacle there)
- Each simulation tracks visited states; if a state repeats, it's a loop

**Answer: 1304**

## Performance Notes

The key optimization for part two is recognizing that obstacles only matter if they're on the guard's path. This reduces the search space from ~17,000 positions (130×130 grid) to just the ~4,789 positions the guard actually visits, making the solution run in reasonable time.

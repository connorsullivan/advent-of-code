# Day 14: Restroom Redoubt

## Part One

### Problem Summary
Simulate robots moving in a 101×103 tile grid with wrapping (teleportation at edges). After 100 seconds, calculate a "safety factor" by counting robots in each quadrant and multiplying the counts.

### Approach
1. **Parse Input**: Extract position `(px, py)` and velocity `(vx, vy)` from each line
2. **Simulate Movement**: Use modular arithmetic to handle wrapping:
   - `final_x = (px + vx * seconds) % width`
   - `final_y = (py + vy * seconds) % height`
3. **Count Quadrants**: Divide the grid into 4 quadrants, ignoring robots on the middle lines (x=50 or y=51)
4. **Calculate Safety Factor**: Multiply the robot counts in all 4 quadrants

### Key Insights
- Wrapping behavior is elegantly handled with modulo operation
- Robots exactly on middle lines (x=width//2 or y=height//2) are excluded from quadrant counting
- No need to simulate step-by-step; can calculate final position directly

**Answer: 226179492**

## Part Two

### Problem Summary
Find the fewest number of seconds until robots arrange themselves into a Christmas tree pattern.

### Approach
1. **Pattern Detection**: Search through time steps to find when robots form a recognizable pattern
2. **Heuristic**: A Christmas tree would have many consecutive robots in horizontal lines (forming the tree shape)
3. **Implementation**:
   - Iterate through seconds (1 to 10,000)
   - For each time step, simulate all robot positions
   - Check if positions contain a line of 10+ consecutive robots (indicating tree structure)
4. **Visualization**: Save the grid visualization when pattern is found

### Key Insights
- The Christmas tree appears when robots align to form dense, connected patterns
- Looking for long consecutive horizontal sequences is an effective heuristic
- The pattern appears at second 7502, showing a clear Christmas tree with:
  - A triangular tree shape made of `#` symbols
  - A border frame around the tree
  - The characteristic wide base and pointed top

**Answer: 7502**

### Visualization
The Christmas tree pattern at 7502 seconds shows a clear ASCII art tree with approximately 30 rows forming a triangular pine tree shape, bordered by vertical lines on the sides.

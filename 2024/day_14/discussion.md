# Day 14: Restroom Redoubt

## Part 1
The problem asks us to simulate the movement of robots in a grid of size 101x103. Each robot has a starting position and a velocity. They wrap around the edges (teleport). We need to find their positions after 100 seconds.

The position of a robot after $t$ seconds can be calculated directly using modular arithmetic:
$x_t = (p_x + v_x \times t) \pmod W$
$y_t = (p_y + v_y \times t) \pmod H$

After calculating the final positions, we count the number of robots in each of the four quadrants. Robots exactly on the middle lines ($x=50$ or $y=51$) are ignored. The answer is the product of the counts in the four quadrants (the safety factor).

## Part 2
We need to find the fewest number of seconds for the robots to display a "Christmas tree". This implies a non-random arrangement of robots.

Since the grid dimensions are 101 and 103 (coprime), the pattern of robot positions repeats every $101 \times 103 = 10403$ seconds. We can iterate through each second $t$ from 1 to 10403 and check for a pattern.

A "Christmas tree" or any picture likely involves a cluster of robots. A good heuristic to detect this is to count the number of robots that have at least one neighbor (up, down, left, or right). The time $t$ with the maximum number of neighbors is likely the answer.

Using this heuristic, we found a significant spike in neighbor counts at $t=7847$. Visualizing the grid at this time confirms a clear picture of a Christmas tree.

## Complexity
- **Part 1**: $O(N)$, where $N$ is the number of robots. We iterate through the robots once.
- **Part 2**: $O(N \times W \times H)$, where $W$ and $H$ are the grid dimensions. We iterate through the period ($W \times H$) and for each step, we check neighbors for all robots. Since $W \times H$ is relatively small (~10k), this is feasible.

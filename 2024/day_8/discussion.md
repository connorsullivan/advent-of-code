# Day 8: Resonant Collinearity

## Part 1

The problem asks us to find "antinodes" created by pairs of antennas with the same frequency. An antinode is formed at a point that is collinear with two antennas and satisfies a specific distance condition (one is twice as far as the other).

Geometrically, for two antennas at positions $A$ and $B$, the antinodes are located at:
1. $P_1 = 2A - B$
2. $P_2 = 2B - A$

These points lie on the line passing through $A$ and $B$, outside the segment $AB$, such that the distance from the closer antenna equals the distance between the antennas.

**Algorithm:**
1.  Parse the input grid to map each frequency character to a list of coordinates.
2.  Initialize a set `antinodes` to store unique valid locations.
3.  For each frequency:
    - Iterate through all unique pairs of antennas $(A, B)$.
    - Calculate the vector $\vec{AB} = B - A$.
    - Calculate potential antinodes: $A - \vec{AB}$ and $B + \vec{AB}$.
    - If an antinode is within the grid boundaries, add it to the set.
4.  Return the size of the set.

**Complexity:**
- Time: $O(K \cdot N_k^2)$, where $K$ is the number of frequencies and $N_k$ is the number of antennas for frequency $k$. In the worst case, this is bounded by the square of the total number of cells, but practically much smaller.
- Space: $O(R \times C)$ to store the grid and antinodes.

## Part 2

The rules change such that an antinode occurs at *any* grid position exactly in line with at least two antennas of the same frequency. This means we need to find all integer coordinates on the line passing through any pair of antennas.

**Algorithm:**
1.  Use the same parsed antenna data.
2.  For each pair of antennas $(A, B)$ of the same frequency:
    - Calculate the vector $\vec{v} = (dr, dc) = B - A$.
    - Simplify the vector to its smallest integer steps by dividing by the greatest common divisor: $g = \gcd(dr, dc)$, $\vec{u} = (dr/g, dc/g)$.
    - Starting from $A$, move in steps of $\vec{u}$ (add $\vec{u}$) until leaving the grid, adding each point to the set.
    - Starting from $A$, move in steps of $-\vec{u}$ (subtract $\vec{u}$) until leaving the grid, adding each point to the set.
3.  Return the size of the set.

**Complexity:**
- Time: $O(K \cdot N_k^2 \cdot D)$, where $D$ is the diagonal length of the grid (max steps).
- Space: $O(R \times C)$.

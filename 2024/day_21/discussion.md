# Day 21: Keypad Conundrum

## Problem Description

We need to control a robot arm on a numeric keypad to type a specific code. However, the robot is controlled by another robot on a directional keypad, which is controlled by another robot on another directional keypad, and so on.

We need to find the shortest sequence of button presses we need to type on our directional keypad to make the final robot type the code on the numeric keypad.

The complexity of a code is the length of the shortest sequence multiplied by the numeric part of the code. We need to find the sum of complexities for all codes.

Part 1 involves 2 intermediate directional keypads (3 robots total).
Part 2 involves 25 intermediate directional keypads (26 robots total).

## Approach

The problem can be modeled as finding the shortest path through a series of transformations. Since the sequence length grows exponentially with the number of robots, we cannot simply generate the full sequence string. Instead, we only need to calculate its length.

### Recursive Expansion with Memoization

We can break down the problem into smaller subproblems. To move a robot arm from button A to button B on a keypad, we need to generate a sequence of moves on the controlling keypad.

Let `Cost(start, end, depth)` be the length of the shortest sequence required on the human's keypad to move the robot at `depth` from `start` to `end` and press the button.

- **Base Case (`depth == 0`)**: The cost is simply the length of the shortest path on the current keypad + 1 (for the 'A' press). This represents the human typing directly.
- **Recursive Step**: To move from `start` to `end` at `depth`, we find all shortest paths on the current keypad (e.g., `v<<A`). For each path, we calculate the cost to type that sequence using the robot at `depth - 1`. The cost is the sum of costs for each transition in the sequence (e.g., `A -> v`, `v -> <`, `< -> <`, `< -> A`). We take the minimum cost among all shortest paths.

We use memoization to store the results of `Cost(start, end, depth)` to avoid recomputing the same subproblems. The state space is small: `(start_key, end_key, depth)`. There are only ~25 transitions on a directional keypad, and `depth` goes up to 25.

### Keypads

**Numeric Keypad (Level `depth`):**
```
7 8 9
4 5 6
1 2 3
  0 A
```
Gap at (0, 3).

**Directional Keypad (Levels `0` to `depth-1`):**
```
  ^ A
< v >
```
Gap at (0, 0).

### Algorithm

1.  **Path Generation**: Precompute or generate on-the-fly all shortest paths between any two keys on a keypad, ensuring we don't cross the gap.
2.  **Cost Calculation**:
    - `solve_code(code, depth)`: Iterates through the code on the Numeric Keypad. For each transition, finds all shortest paths. For each path, calculates the cost using `get_dirpad_cost(..., depth - 1)`. Takes the minimum.
    - `get_dirpad_cost(start, end, depth)`: Memoized function. Finds all shortest paths on the Directional Keypad. For each path, calculates the cost recursively using `get_dirpad_cost(..., depth - 1)`.

### Complexity

- **Time Complexity**: `O(N * M * D)`, where `N` is the length of the code, `M` is the number of transitions on the keypad (constant), and `D` is the depth (number of robots). With memoization, we only compute each state once.
- **Space Complexity**: `O(M * D)` for the memoization cache.

## Results

- **Part 1**: 123096
- **Part 2**: 154517692795352

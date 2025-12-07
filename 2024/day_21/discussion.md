# Day 21: Keypad Conundrum

## Problem Overview

This problem involves a chain of robots controlling each other through keypads to ultimately type codes on a numeric keypad. We need to find the minimum number of button presses required at the human level to cause the final robot to type each code.

## Approach

### Key Insights

1. **Keypad Layouts**:
   - Numeric keypad: 3x3 grid with 0-9, plus A, with a gap at bottom-left
   - Directional keypad: Arrow keys (^, v, <, >) plus A, with a gap at top-left

2. **Chain of Control**:
   - Part 1: Human → Directional Robot 1 → Directional Robot 2 → Numeric Robot
   - Part 2: Same structure but with 25 directional robots instead of 2

3. **Path Finding**: From any button to another, there may be multiple shortest paths. However, not all paths are valid—they must not pass through the gap positions.

4. **Recursive Structure**: The problem has a natural recursive structure—to type a character at depth N, we need to move the robot at depth N+1, which requires typing on the keypad at depth N+2, and so on.

### Algorithm

1. **Generate Valid Moves**: For each pair of buttons on a keypad, generate all possible shortest move sequences that avoid the gap position. These sequences consist of directional moves (^, v, <, >) followed by 'A' to press the button.

2. **Dynamic Programming with Memoization**: Use `@lru_cache` to memoize the `get_sequence_length` function, which calculates the minimum button presses needed to type a sequence at a given depth.

3. **Recursive Calculation**:
   - At depth 0 (numeric keypad), we need to type the actual code
   - At each subsequent depth (directional keypads), we need to type the move sequences from the previous depth
   - At the final depth (human level), we count the actual button presses

4. **Optimization**: The key optimization is choosing the move sequence at each step that results in the minimum cost at the next depth. Since different orderings of moves (e.g., ">>^" vs "^>>") may have different costs when typed on a directional keypad, we try all valid permutations.

### Implementation Details

- **Path Validation**: When generating move sequences, we simulate each path to ensure it doesn't pass through the gap position.
- **Complexity Calculation**: Multiply the sequence length by the numeric part of the code (ignoring leading zeros and the 'A').
- **Memoization**: Critical for Part 2 with 26 robot depths—without it, the solution would be intractably slow.

## Results

- **Part One** (3 robots): 176,870
- **Part Two** (26 robots): 223,902,935,165,512

The exponential growth in sequence length from Part 1 to Part 2 demonstrates why the recursive memoization approach is essential. The final answer for Part 2 is over 200 trillion button presses!

## Part One

Implemented a recursive solution with memoization to calculate the minimum button presses needed through a chain of 3 robots (2 directional + 1 numeric). The solution correctly handles path finding while avoiding gaps and optimizes by trying all valid move orderings.

## Part Two

Extended the solution to handle 26 robots (25 directional + 1 numeric). The memoization ensures the solution runs efficiently despite the massive increase in depth, as many subsequences are reused across different codes and positions.

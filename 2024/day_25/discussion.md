# Day 25 Solutions

## Part 1

The goal is to find the number of unique lock/key pairs that fit together without overlapping.

### Approach

1.  **Parsing**: The input contains schematics for locks and keys.
    -   **Locks** have the top row filled (`#####`).
    -   **Keys** have the top row empty (`.....`).
    -   We convert each schematic into a tuple of heights. The height for a column is calculated as the total number of `#` characters in that column minus 1. This works because locks extend down from the top and keys extend up from the bottom, and the "height" represents the extension into the 5 available spaces between the top and bottom rows.

2.  **Matching**:
    -   We iterate through every possible pair of (lock, key).
    -   A pair fits if, for every column, the sum of the lock's pin height and the key's shape height is less than or equal to 5 (the available space).
    -   `lock_height[i] + key_height[i] <= 5`

3.  **Counting**: We count the number of pairs that satisfy the condition.

### Complexity

-   **Time Complexity**: $O(L \times K \times W)$, where $L$ is the number of locks, $K$ is the number of keys, and $W$ is the width (5). Since $L + K = N$ (total input blocks), this is roughly $O(N^2)$. With $N \approx 4000$, $N^2 \approx 1.6 \times 10^7$ operations, which is fast enough.
-   **Space Complexity**: $O(N \times W)$ to store the parsed heights.

## Part 2

Day 25 traditionally does not have a second puzzle part. The second star is awarded for completing all previous 49 stars and finishing the event.

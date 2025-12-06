# Day 11 Solutions

## Part 1

The problem asks us to simulate the evolution of stones based on a set of rules over 25 blinks. The number of stones grows as stones can split.

### Approach

We can model the stones as a collection of numbers. Since the order of stones does not affect how they evolve (each stone evolves independently), and we only need the total count of stones at the end, we can optimize the simulation.

Instead of maintaining a list of all stones (which would grow exponentially), we can maintain a count of each unique stone number using a hash map (or `Counter`).

For each blink:
1. Iterate through the current unique stone numbers and their counts.
2. Apply the transformation rules to each number.
3. Add the resulting new stones to a new counter, multiplying their occurrence by the count of the original stone.

**Rules:**
- 0 becomes 1.
- Even number of digits: split into two stones (left half, right half).
- Else: multiply by 2024.

After 25 blinks, the sum of all counts in the map is the answer.

## Part 2

Part 2 asks for the number of stones after 75 blinks.

### Approach

The approach used in Part 1 is efficient enough for Part 2. The number of unique stone values remains manageable even as the total number of stones becomes massive. The complexity depends on the number of unique stone values generated, not the total number of stones.

Using the `Counter` approach:
- **Time Complexity**: Proportional to (number of blinks) * (number of unique stone values).
- **Space Complexity**: Proportional to the number of unique stone values.

This allows us to calculate the result for 75 blinks almost instantly.

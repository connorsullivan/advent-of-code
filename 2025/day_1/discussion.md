# Day 1

## Part One

The first part requires tracking a dial that starts at position 50 and follows rotation instructions. Each instruction is either 'L' (left/lower numbers) or 'R' (right/higher numbers) followed by a distance. The dial has positions 0-99 in a circle.

The solution:
1. Start at position 50
2. For each rotation, calculate the new position using modulo 100 to handle the circular nature
3. Count how many times we land exactly on 0 after completing a rotation

Time complexity: O(n) where n is the number of instructions.

## Part Two

Part two requires counting not just when we end at 0, but every time we pass through 0 during any rotation. For example, rotating right 150 positions would pass through 0 once during the rotation, in addition to possibly ending at 0.

The solution:
1. Start at position 50
2. For each rotation, instead of jumping directly to the final position, simulate clicking through each position one at a time
3. Count every time position equals 0, whether during or at the end of a rotation

Time complexity: O(n × d) where n is the number of instructions and d is the average distance per instruction.

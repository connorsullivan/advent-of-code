# Day 1

## Part One

The puzzle involves simulating a dial that rotates left (L) or right (R) on a circular dial with numbers 0-99. Starting at position 50, we track rotations and count how many times the dial ends at position 0 after a complete rotation.

The solution is straightforward: for each instruction, we update the position using modular arithmetic (`(position +/- distance) % 100`) and count when the final position is 0.

## Part Two

Part 2 extends the problem to count every time the dial passes through or lands on 0 during any rotation, not just at the end. Key insights:
- Full rotations (distance >= 100) contribute `distance // 100` passes through 0
- For partial rotations: when moving left from position, we hit 0 if `remaining >= position` (and position > 0); when moving right, we hit 0 if `position + remaining >= 100`
- Starting at position 0 and moving away doesn't count as hitting 0

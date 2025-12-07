# Day 13: Claw Contraption

## Part One

This problem involves determining the minimum number of tokens needed to win prizes from claw machines. Each machine has:
- Button A: Moves the claw by a certain amount in X and Y directions (costs 3 tokens)
- Button B: Moves the claw by a different amount in X and Y directions (costs 1 token)
- Prize: Located at specific X and Y coordinates

The goal is to find how many times to press each button to reach the exact prize location.

### Approach

This is a classic **system of linear equations** problem. For each machine, we need to solve:
- `a × ax + b × bx = px`
- `a × ay + b × by = py`

Where:
- `a` = number of times to press Button A
- `b` = number of times to press Button B
- `(ax, ay)` = movement deltas for Button A
- `(bx, by)` = movement deltas for Button B
- `(px, py)` = prize coordinates

### Solution Method

I used **Cramer's Rule** to solve the system:

1. Calculate the determinant: `det = ax × by - ay × bx`
2. If det = 0, there's no unique solution
3. Calculate: `a = (px × by - py × bx) / det`
4. Calculate: `b = (ax × py - ay × px) / det`
5. Check if `a` and `b` are non-negative integers

If valid solutions exist, calculate cost: `3a + b` tokens.

**Result: 36,838 tokens**

## Part Two

Part Two adds a twist: due to a "unit conversion error," we must add 10,000,000,000,000 to both the X and Y coordinates of every prize.

### Key Insight

The same mathematical approach works even with these enormous coordinates! The beauty of using linear algebra (Cramer's Rule) is that it handles large numbers efficiently without needing iterative searching. The algorithm remains O(1) per machine.

The large offset makes many previously winnable prizes impossible (buttons can't reach that far), but some remain solvable. The mathematical solution finds exact integer solutions directly.

**Result: 83,029,436,920,891 tokens**

### Implementation Notes

- Used regex to parse input (Button A/B movements and Prize coordinates)
- Integer division (`//`) ensures we only accept exact integer solutions
- Modulo check (`%`) verifies that solutions are indeed integers before dividing
- Non-negativity check ensures physical validity (can't press buttons negative times)

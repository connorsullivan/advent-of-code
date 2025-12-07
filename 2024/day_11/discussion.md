# Day 11: Plutonian Pebbles

## Problem Summary
We observe stones arranged in a line, each with a number engraved on it. Every time we blink, the stones transform simultaneously according to these rules:
1. If the stone is 0, it becomes 1
2. If the stone has an even number of digits, it splits into two stones (left half and right half of digits)
3. Otherwise, the stone's number is multiplied by 2024

**Part One**: Count stones after 25 blinks
**Part Two**: Count stones after 75 blinks

## Approach

### Part One: Brute Force Simulation
For 25 blinks, we can use a straightforward simulation approach:
- Maintain a list of current stones
- For each blink, apply the transformation rules to each stone
- Replace the list with the new stones
- Return the count after 25 iterations

This works because 25 blinks doesn't produce an unmanageable number of stones.

### Part Two: Memoization/Dynamic Programming
For 75 blinks, the brute force approach would be too slow due to exponential growth. The key insight is that:
- **Each stone evolves independently** of other stones
- The same stone value produces the same sequence of transformations
- We can use **memoization** to cache the count of stones produced by each (stone, blinks_remaining) pair

The recursive memoized function:
```python
@cache
def count_stones_after_blinks(stone, blinks_remaining):
    if blinks_remaining == 0:
        return 1

    # Apply transformation rule and recursively count
    # Cache prevents recomputing the same (stone, blinks) pair
```

This dramatically reduces computation time from exponential to polynomial complexity.

## Key Insights
1. **Order doesn't matter for counting**: We only need to count stones, not track their positions
2. **Independent evolution**: Each stone's transformation is independent of others
3. **Repeated patterns**: The same stone value will always produce the same sequence, making memoization highly effective
4. **Digit splitting**: When splitting even-digit numbers, leading zeros are removed (e.g., 1000 → 10 and 0)

## Results
- **Part One**: 216,996 stones after 25 blinks
- **Part Two**: 257,335,372,288,947 stones after 75 blinks

The massive difference between parts 1 and 2 (from ~217K to ~257 trillion) demonstrates the exponential growth and why the memoized approach is essential for part 2.

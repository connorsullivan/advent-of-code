# Day 25

## Part One

This problem involves matching lock and key schematics to find compatible pairs.

### Understanding the Problem

The input consists of 7-line schematics representing either locks or keys:
- **Locks**: Top row is `#####` (filled), bottom row is `.....` (empty)
- **Keys**: Bottom row is `#####` (filled), top row is `.....` (empty)

Each schematic represents a 5-column pin/key configuration with varying heights.

### Approach

1. **Parse Input**: Split the input into individual schematics (separated by blank lines)

2. **Classify Schematics**:
   - Check the first row: if `#####`, it's a lock
   - Check the last row: if `#####`, it's a key

3. **Convert to Heights**:
   - **For locks**: Count consecutive `#` symbols in each column from top (excluding the top row itself)
   - **For keys**: Count consecutive `#` symbols in each column from bottom (excluding the bottom row itself)
   - This gives us 5 height values per schematic

4. **Test Compatibility**:
   - For each lock/key pair, check all 5 columns
   - A pair fits if `lock_height[col] + key_height[col] ≤ 5` for all columns
   - The constraint of ≤ 5 comes from the total available space (7 rows - 2 boundary rows = 5 rows)

5. **Count Compatible Pairs**: Count all lock/key combinations that don't overlap

### Example
From the problem:
- Lock `0,5,3,4,3` and Key `3,0,2,0,1`: All columns fit (0+3=3, 5+0=5, 3+2=5, 4+0=4, 3+1=4, all ≤5) ✓
- Lock `0,5,3,4,3` and Key `5,0,2,1,3`: Overlap in last column (3+3=6 > 5) ✗

### Result
The solution found **3317** unique lock/key pairs that fit together without overlapping.

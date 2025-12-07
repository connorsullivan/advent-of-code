# Day 3: Mull It Over

## Part One

The challenge is to parse corrupted memory and extract valid `mul(X,Y)` instructions where X and Y are 1-3 digit numbers, then sum all the products.

**Approach:**
- Used regular expressions to find all valid `mul(X,Y)` patterns
- Pattern: `mul\((\d{1,3}),(\d{1,3})\)`
- This ensures only properly formatted instructions with 1-3 digit numbers are matched
- Invalid formats like `mul(4*`, `mul(6,9!`, `?(12,34)`, or `mul ( 2 , 4 )` are ignored
- Summed all products from valid matches

**Result:** 175015740

## Part Two

Part 2 adds conditional instructions that enable/disable multiplication:
- `do()` enables future mul instructions
- `don't()` disables future mul instructions
- mul instructions start enabled at the beginning

**Approach:**
- Extended the regex pattern to match `mul(X,Y)`, `do()`, and `don't()` instructions
- Used `re.finditer()` to process matches in order (important for tracking state)
- Maintained an `enabled` flag (starts as True)
- When encountering `do()`, set enabled to True
- When encountering `don't()`, set enabled to False
- Only process `mul(X,Y)` instructions when enabled is True
- Sum only the products from enabled multiplications

**Key Insight:** The order of instructions matters. We must process them sequentially to correctly track the enabled/disabled state at each point in the corrupted memory.

**Result:** 112272912

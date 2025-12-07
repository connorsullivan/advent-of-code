# Day 17: Chronospatial Computer

## Part One

**Problem**: Simulate a 3-bit computer with three registers (A, B, C) and eight instructions. Execute the given program and collect all output values.

**Approach**:
- Built a computer simulator that processes instructions based on an instruction pointer
- Implemented all 8 opcodes:
  - **0 (adv)**: Divide A by 2^combo_operand → A
  - **1 (bxl)**: B XOR literal_operand → B
  - **2 (bst)**: combo_operand mod 8 → B
  - **3 (jnz)**: Jump to literal_operand if A ≠ 0
  - **4 (bxc)**: B XOR C → B
  - **5 (out)**: Output combo_operand mod 8
  - **6 (bdv)**: A / 2^combo_operand → B
  - **7 (cdv)**: A / 2^combo_operand → C
- Combo operands: 0-3 are literals, 4-6 are registers A-C respectively
- The instruction pointer advances by 2 after each instruction (except jumps)

**Answer**: `2,0,4,2,7,0,1,0,3`

## Part Two

**Problem**: Find the lowest positive initial value for register A that causes the program to output a copy of itself.

**Approach**:
The key insight is that the program processes A by repeatedly dividing it by 8 (right-shifting 3 bits), which means each output digit depends on a specific 3-bit segment of A's binary representation.

**Strategy - Working Backwards**:
1. Start from the last digit of the program output
2. For each position (from end to beginning):
   - Take each candidate value found so far
   - Try all 8 possible 3-bit extensions (0-7)
   - Shift the candidate left by 3 bits and OR with each extension
   - Test if this new value produces the correct output suffix
   - Keep only values that match
3. Return the smallest valid value

This works because:
- Each iteration of the program loop outputs one digit based on the current A value
- Then A is divided by 8 (shifting right 3 bits)
- By building A from right to left (3 bits at a time), we ensure each segment produces the correct output digit
- We validate the entire suffix at each step to ensure consistency

**Answer**: `265601188299675`

This value, when used as the initial register A, causes the program to output: `2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0` which exactly matches the program itself.

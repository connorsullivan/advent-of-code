# Day 24: Crossed Wires

## Problem Summary

This puzzle involves simulating a circuit of logic gates (AND, OR, XOR) that processes binary inputs through a series of interconnected gates.

**Part 1**: Simulate the circuit with given initial wire values and gate connections, then calculate the decimal number represented by all wires starting with 'z'.

**Part 2**: The circuit is supposed to be a binary adder (adding x-wires and y-wires to produce z-wires), but exactly 4 pairs of gate outputs have been swapped. Find which 8 wires are involved in these swaps.

## Approach

### Part One: Circuit Simulation

The solution uses a queue-based simulation:

1. **Parse the input** into two parts:
   - Initial wire values (e.g., `x00: 1`)
   - Gate definitions (e.g., `x00 AND y00 -> z00`)

2. **Simulate using a queue**:
   - Start with gates that need processing
   - For each gate, check if both inputs are available
   - If not, re-queue the gate for later
   - If yes, compute the output based on the operation (AND, OR, XOR)
   - Continue until all gates have been processed

3. **Extract the result**:
   - Collect all wires starting with 'z'
   - Sort them (z00, z01, z02, ...)
   - Treat them as a binary number (z00 is LSB)
   - Convert to decimal

### Part Two: Finding Swapped Gates

This part requires understanding the structure of a ripple-carry adder:

**Ripple-Carry Adder Structure:**
- For bit 0: `z0 = x0 XOR y0`, `carry0 = x0 AND y0`
- For bit i > 0:
  - `xor_xy = xi XOR yi`
  - `and_xy = xi AND yi`
  - `zi = xor_xy XOR carry_in`
  - `and_carry = xor_xy AND carry_in`
  - `carry_out = and_xy OR and_carry`

**Detection Strategy:**

The solution identifies violations of the expected adder structure:

1. **Z-wire check**: All z outputs (except the final carry) must be XOR gates
   - Violation indicates that wire is swapped

2. **XOR gate checks**:
   - XOR with x/y inputs (first level) should either:
     - Go to z00 (for bit 0)
     - Feed into both XOR and AND gates (for higher bits)
     - NOT go directly to other z outputs
   - XOR with intermediate inputs (second level) must go to a z output
   - Violation indicates the output wire is swapped

3. **AND gate checks**:
   - AND outputs (except x00 AND y00) should feed into OR gates
   - Violation indicates the AND output is swapped

4. **OR gate checks**:
   - OR outputs should never go directly to z (except possibly the MSB carry)
   - Violation indicates the OR output is swapped

By checking these structural constraints, we identify exactly 8 wires that violate the adder pattern, representing 4 swapped pairs.

## Results

- **Part One**: `42883464055378`
- **Part Two**: `dqr,dtk,pfw,shh,vgs,z21,z33,z39`

## Key Insights

1. Part 1 is straightforward - just simulate the circuit with a dependency-aware queue
2. Part 2 requires recognizing that the circuit is supposed to be a ripple-carry adder
3. Swapped gates create structural violations that can be detected by checking expected gate patterns
4. The pattern-based approach is more robust than trying to trace through individual bits
5. Each violation corresponds to exactly one swapped wire, making it easy to identify all 8

# Day 24 Solutions

## Part 1

The problem asks us to simulate a system of boolean logic gates (AND, OR, XOR) to produce a final binary number from wires starting with `z`.

### Approach

1.  **Parsing**: We parse the initial wire values into a dictionary and the gate definitions into a list or dictionary.
2.  **Simulation**: Since the problem guarantees no loops, we can simulate the circuit. I used a recursive approach with memoization (or simply a topological evaluation) to compute the value of each `z` wire.
    *   For each `z` wire (from `z00` to `z45`), we recursively evaluate its input gate.
    *   The base cases are the initial wire values provided in the input.
    *   We store computed values to avoid re-computation.
3.  **Result**: We concatenate the bits from `z` wires (from highest index to lowest) to form a binary string and convert it to a decimal integer.

## Part 2

The system is actually a Ripple Carry Adder performing addition of `x` and `y` inputs. However, 4 pairs of gates have their outputs swapped. We need to identify these swapped wires.

### Approach

Instead of simulating the addition for all possible inputs (which is infeasible), we inspect the structure of the circuit to find deviations from a standard Full Adder design.

A Full Adder for bit `i` typically has this structure:
*   `x_i XOR y_i -> inter_xor`
*   `x_i AND y_i -> inter_and`
*   `inter_xor XOR carry_in -> z_i`
*   `inter_xor AND carry_in -> carry_inter`
*   `inter_and OR carry_inter -> carry_out`

We applied the following heuristic rules to identify swapped wires:
1.  **Z-wire Rule**: Any gate outputting to a `z` wire (except the MSB `z45`) MUST be an XOR gate. If not, the output wire is swapped.
2.  **XOR-gate Rule**: Any XOR gate that does not output to a `z` wire MUST have `x` and `y` as inputs. If an XOR gate has intermediate inputs but does not output to `z`, it is swapped.
3.  **AND-gate Rule**: Any AND gate (except for the very first half-adder `x00 AND y00`) must output to an OR gate. If it outputs to anything else, it is swapped.
4.  **Intermediate XOR Rule**: The output of `x XOR y` (except for `x00 XOR y00`) must feed into an XOR gate (to produce `z`) and an AND gate. It must NOT feed into an OR gate.

By applying these rules, we identified exactly 8 wires that violated the structure, which corresponds to the 4 swapped pairs. Sorting these wire names gives the answer.

### Complexity
*   **Time Complexity**: O(N), where N is the number of gates. We iterate through the gates a constant number of times to check the rules.
*   **Space Complexity**: O(N) to store the gate definitions and usage maps.

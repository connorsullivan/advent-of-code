# Day 17 Solutions

## Part 1

The problem asks us to simulate a 3-bit computer with 3 registers (A, B, C) and 8 instructions. The program is a sequence of 3-bit opcodes and operands.

### Approach

I implemented a `Computer` class that maintains the state of the registers and the instruction pointer. The `run` method executes the program loop:
1.  Fetch opcode and operand at the current instruction pointer.
2.  Execute the instruction based on the opcode definitions.
3.  Update the instruction pointer (usually +2, unless it's a jump).
4.  Collect outputs.
5.  Halt when the instruction pointer goes out of bounds.

The `part_one` function parses the input, initializes the computer, and returns the comma-separated output string.

## Part 2

We need to find the lowest positive initial value for register A that causes the program to output a copy of itself.

### Approach

The program loop effectively processes register A in 3-bit chunks. In each iteration, `A` is shifted right by 3 bits (`adv 3`). The output depends on the current value of A (specifically, the lowest 3 bits and some higher bits used in `bxc` and `cdv` instructions).

Since the program length is 16, and each iteration consumes roughly 3 bits of A, the initial A must be roughly $8^{15}$ to $8^{16}$.

I used a reverse search algorithm (Breadth-First Search):
1.  We want to construct A such that the output matches the program from the end to the beginning.
2.  Start with `candidates = [0]`.
3.  Iterate from the last instruction of the program to the first (16 steps).
4.  In each step, for each `val` in `candidates`, try all possible 3-bit values `k` (0-7).
5.  Construct `new_val = val * 8 + k`.
6.  Run the program with `A = new_val`.
7.  Check if the output matches the expected suffix of the program.
8.  If it matches, add `new_val` to the next set of candidates.
9.  After 16 steps, the candidates in the list are valid initial values for A that produce the entire program.
10. The answer is the minimum value in the final candidates list.

This approach is efficient because it prunes the search space significantly at each step, only keeping prefixes that produce the correct suffix of the output.

**Time Complexity:** $O(N \cdot 8)$, where $N$ is the length of the program. In practice, the number of candidates at each step is small.
**Space Complexity:** $O(1)$ (or proportional to the number of surviving candidates).

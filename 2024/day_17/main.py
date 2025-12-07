import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    """Parse the input to extract register values and program."""
    register_a = int(lines[0].split(": ")[1])
    register_b = int(lines[1].split(": ")[1])
    register_c = int(lines[2].split(": ")[1])
    program = list(map(int, lines[4].split(": ")[1].split(",")))
    return register_a, register_b, register_c, program

def get_combo_value(operand, registers):
    """Get the value of a combo operand."""
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    else:
        raise ValueError(f"Invalid combo operand: {operand}")

def run_program(register_a, register_b, register_c, program):
    """Run the 3-bit computer program and return the output."""
    registers = {'A': register_a, 'B': register_b, 'C': register_c}
    ip = 0  # instruction pointer
    output = []

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:  # adv - divide A by 2^combo_operand, store in A
            combo = get_combo_value(operand, registers)
            registers['A'] = registers['A'] // (2 ** combo)
        elif opcode == 1:  # bxl - XOR B with literal operand, store in B
            registers['B'] = registers['B'] ^ operand
        elif opcode == 2:  # bst - combo operand mod 8, store in B
            combo = get_combo_value(operand, registers)
            registers['B'] = combo % 8
        elif opcode == 3:  # jnz - jump if A != 0
            if registers['A'] != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc - XOR B with C, store in B
            registers['B'] = registers['B'] ^ registers['C']
        elif opcode == 5:  # out - output combo operand mod 8
            combo = get_combo_value(operand, registers)
            output.append(combo % 8)
        elif opcode == 6:  # bdv - divide A by 2^combo_operand, store in B
            combo = get_combo_value(operand, registers)
            registers['B'] = registers['A'] // (2 ** combo)
        elif opcode == 7:  # cdv - divide A by 2^combo_operand, store in C
            combo = get_combo_value(operand, registers)
            registers['C'] = registers['A'] // (2 ** combo)

        ip += 2

    return output

def part_one(lines):
    register_a, register_b, register_c, program = parse_input(lines)
    output = run_program(register_a, register_b, register_c, program)
    return ','.join(map(str, output))

def part_two(lines):
    _, register_b, register_c, program = parse_input(lines)

    # The program needs to output itself, so we need to find the right initial value for A
    # The program outputs values one at a time, and each output depends on A's value
    # Since the program divides A by 8 (shifts right 3 bits) in each iteration,
    # we can work backwards from the end of the program

    # Start with possible values that produce the last digit
    candidates = [0]

    # Work backwards through the program output
    for i in range(len(program) - 1, -1, -1):
        next_candidates = []
        target = program[i]

        # For each candidate so far, try all possible 3-bit extensions
        for candidate in candidates:
            for bits in range(8):
                test_a = (candidate << 3) | bits
                output = run_program(test_a, register_b, register_c, program)

                # Check if this produces the correct suffix of the program
                if len(output) >= len(program) - i and output[0] == target:
                    # Verify it matches the entire suffix we've built so far
                    expected_suffix = program[i:]
                    if output[:len(expected_suffix)] == expected_suffix:
                        next_candidates.append(test_a)

        candidates = next_candidates
        if not candidates:
            break

    # Return the smallest valid value
    return min(candidates) if candidates else None

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

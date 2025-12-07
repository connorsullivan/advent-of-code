import sys
import os
from collections import deque

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    """Parse the input into initial wire values and gate definitions"""
    wires = {}
    gates = []

    i = 0
    # Parse initial wire values
    while i < len(lines) and lines[i].strip():
        line = lines[i].strip()
        if ':' in line:
            wire, value = line.split(': ')
            wires[wire] = int(value)
        i += 1

    # Skip blank line
    i += 1

    # Parse gate definitions
    while i < len(lines):
        line = lines[i].strip()
        if line:
            parts = line.split(' -> ')
            output = parts[1]
            gate_parts = parts[0].split()
            input1, op, input2 = gate_parts[0], gate_parts[1], gate_parts[2]
            gates.append((input1, op, input2, output))
        i += 1

    return wires, gates

def simulate_circuit(wires, gates):
    """Simulate the circuit until all gates have produced outputs"""
    wires = wires.copy()  # Don't modify original
    pending_gates = deque(gates)

    while pending_gates:
        input1, op, input2, output = pending_gates.popleft()

        # Check if both inputs are available
        if input1 not in wires or input2 not in wires:
            pending_gates.append((input1, op, input2, output))
            continue

        val1 = wires[input1]
        val2 = wires[input2]

        # Calculate output based on operation
        if op == 'AND':
            result = val1 & val2
        elif op == 'OR':
            result = val1 | val2
        elif op == 'XOR':
            result = val1 ^ val2
        else:
            raise ValueError(f"Unknown operation: {op}")

        wires[output] = result

    return wires

def get_z_value(wires):
    """Extract the decimal value from all z wires"""
    z_wires = [(wire, value) for wire, value in wires.items() if wire.startswith('z')]
    z_wires.sort()  # Sort by wire name (z00, z01, z02, ...)

    binary_str = ''.join(str(value) for _, value in reversed(z_wires))
    return int(binary_str, 2)

def part_one(lines):
    wires, gates = parse_input(lines)
    wires = simulate_circuit(wires, gates)
    return get_z_value(wires)

def find_gate_by_output(gates, output):
    """Find a gate by its output wire"""
    for gate in gates:
        if gate[3] == output:
            return gate
    return None

def find_gates_by_inputs(gates, input1, input2, op=None):
    """Find gates by their input wires (order independent) and optionally operation"""
    result = []
    for gate in gates:
        gate_inputs = {gate[0], gate[2]}
        if gate_inputs == {input1, input2}:
            if op is None or gate[1] == op:
                result.append(gate)
    return result

def part_two(lines):
    """Find the 4 pairs of swapped gate outputs in an adder circuit"""
    wires, gates = parse_input(lines)

    # Build lookup structures
    gate_by_output = {}
    for gate in gates:
        gate_by_output[gate[3]] = gate

    def find_gate(in1, in2, op):
        """Find a gate with specific inputs and operation (order independent)"""
        for gate in gates:
            if gate[1] == op and {gate[0], gate[2]} == {in1, in2}:
                return gate
        return None

    def get_output(in1, in2, op):
        """Get the output wire for a gate with specific inputs and operation"""
        if in1 is None or in2 is None:
            return None
        gate = find_gate(in1, in2, op)
        return gate[3] if gate else None

    wrong = set()

    # Determine number of bits
    x_wires = [w for w in wires if w.startswith('x')]
    num_bits = len(x_wires)

    # For a ripple-carry adder:
    # Each bit i (except bit 0) needs:
    # 1. xor_xy = xi XOR yi
    # 2. and_xy = xi AND yi
    # 3. zi = xor_xy XOR carry_in
    # 4. and_carry = xor_xy AND carry_in
    # 5. carry_out = and_xy OR and_carry

    # Check each z output
    for i in range(num_bits):
        z_wire = f'z{i:02d}'

        if z_wire in gate_by_output:
            gate = gate_by_output[z_wire]
            op = gate[1]

            # All z outputs (except the last carry) should be XOR gates
            if i < num_bits and op != 'XOR':
                wrong.add(z_wire)

    # Check intermediate gates
    for gate in gates:
        in1, op, in2, out = gate

        # XOR gates
        if op == 'XOR':
            # XOR gates should either:
            # 1. Have x and y inputs (first level)
            # 2. Have one input from another gate and output to z (second level)
            is_xy_xor = (in1[0] in 'xy' and in2[0] in 'xy')
            is_output_z = out[0] == 'z'

            # If both inputs are from x/y
            if is_xy_xor:
                # If it's bit 0, it should go to z00
                if {in1, in2} == {'x00', 'y00'} and out != 'z00':
                    wrong.add(out)
                # If it's not bit 0, it should NOT go directly to z
                elif {in1, in2} != {'x00', 'y00'} and is_output_z:
                    wrong.add(out)
                # Also, if it's not bit 0 and not going to z, it should be used in XOR and AND
                elif {in1, in2} != {'x00', 'y00'} and not is_output_z:
                    # Check if output feeds into XOR and AND gates
                    feeds_xor = any(g[1] == 'XOR' and out in {g[0], g[2]} for g in gates)
                    feeds_and = any(g[1] == 'AND' and out in {g[0], g[2]} for g in gates)
                    if not (feeds_xor and feeds_and):
                        wrong.add(out)
            else:
                # XOR with intermediate values should go to z
                if not is_output_z:
                    wrong.add(out)

        # AND gates
        elif op == 'AND':
            # AND gate outputs should go to OR gates (except x00 AND y00)
            is_x00_y00 = {in1, in2} == {'x00', 'y00'}
            if not is_x00_y00:
                # Check if this AND output goes to an OR gate
                feeds_or = any(g[1] == 'OR' and out in {g[0], g[2]} for g in gates)
                if not feeds_or:
                    wrong.add(out)

        # OR gates
        elif op == 'OR':
            # OR gate outputs should go to XOR and AND gates (as carry)
            # OR output should NOT go directly to z (except possibly the last bit)
            if out[0] == 'z' and out != f'z{num_bits:02d}':
                wrong.add(out)

    return ','.join(sorted(wrong))

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

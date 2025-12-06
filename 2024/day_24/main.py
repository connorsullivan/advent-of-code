import sys
import os
import re

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    wires = {}
    gates = {}
    parsing_gates = False

    for line in lines:
        line = line.strip()
        if not line:
            parsing_gates = True
            continue

        if not parsing_gates:
            parts = line.split(': ')
            wires[parts[0]] = int(parts[1])
        else:
            # x00 AND y00 -> z00
            match = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', line)
            if match:
                input1, op, input2, output = match.groups()
                gates[output] = (input1, op, input2)

    return wires, gates

def evaluate(wire, wires, gates):
    if wire in wires:
        return wires[wire]

    if wire not in gates:
        raise ValueError(f"Wire {wire} has no value and no gate definition")

    input1, op, input2 = gates[wire]

    val1 = evaluate(input1, wires, gates)
    val2 = evaluate(input2, wires, gates)

    result = 0
    if op == 'AND':
        result = val1 & val2
    elif op == 'OR':
        result = val1 | val2
    elif op == 'XOR':
        result = val1 ^ val2

    wires[wire] = result
    return result

def part_one(lines):
    wires, gates = parse_input(lines)

    z_wires = sorted([w for w in gates.keys() if w.startswith('z')])

    binary_result = ""
    # z00 is least significant, so we want to process from z00 upwards,
    # but binary strings are usually MSB first.
    # "z00 is the least significant bit, then z01, then z02, and so on."
    # So z00 is 2^0, z01 is 2^1.
    # If we build a string, z00 should be at the end.

    for wire in reversed(z_wires):
        val = evaluate(wire, wires, gates)
        binary_result += str(val)

    return int(binary_result, 2)

def part_two(lines):
    wires, gates_dict = parse_input(lines)

    # Convert gates_dict to list of dicts for easier processing
    gates = []
    for out, (in1, op, in2) in gates_dict.items():
        gates.append({'in1': in1, 'op': op, 'in2': in2, 'out': out})

    # Build usage map
    usage = {}
    for i, g in enumerate(gates):
        for inp in [g['in1'], g['in2']]:
            if inp not in usage:
                usage[inp] = []
            usage[inp].append(i)

    swapped = set()

    # Find max z
    z_wires = [g['out'] for g in gates if g['out'].startswith('z')]
    max_z = max(z_wires)

    for g in gates:
        out = g['out']
        op = g['op']
        in1 = g['in1']
        in2 = g['in2']

        # Rule 1: If output is z, op must be XOR. (Except last z)
        if out.startswith('z') and out != max_z:
            if op != 'XOR':
                swapped.add(out)

        # Rule 2: If op is XOR and output is not z, inputs must be x, y.
        if op == 'XOR' and not out.startswith('z'):
            is_xy = (in1.startswith('x') or in1.startswith('y')) and (in2.startswith('x') or in2.startswith('y'))
            if not is_xy:
                swapped.add(out)

        # Rule 3: If op is AND and inputs are not x00, y00, output must go to OR.
        if op == 'AND':
            is_x00_y00 = 'x00' in [in1, in2] and 'y00' in [in1, in2]
            if not is_x00_y00:
                if out in usage:
                    for usage_idx in usage[out]:
                        next_gate = gates[usage_idx]
                        if next_gate['op'] != 'OR':
                            swapped.add(out)

        # Rule 4: If op is XOR and inputs are x, y (and not x00, y00), output must NOT go to OR.
        if op == 'XOR':
            is_xy = (in1.startswith('x') or in1.startswith('y')) and (in2.startswith('x') or in2.startswith('y'))
            is_x00_y00 = 'x00' in [in1, in2] and 'y00' in [in1, in2]
            if is_xy and not is_x00_y00:
                 if out in usage:
                    for usage_idx in usage[out]:
                        next_gate = gates[usage_idx]
                        if next_gate['op'] == 'OR':
                            swapped.add(out)

    return ",".join(sorted(list(swapped)))

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))

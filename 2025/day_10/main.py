import sys
import os
import re
from fractions import Fraction

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_machines(lines):
    machines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Parse indicator light diagram
        diagram_match = re.search(r'\[([.#]+)\]', line)
        diagram = diagram_match.group(1)

        # Parse button wiring schematics
        buttons = []
        button_matches = re.findall(r'\((\d+(?:,\d+)*)\)', line)
        for bm in button_matches:
            buttons.append([int(x) for x in bm.split(',')])

        # Parse joltage requirements
        joltage_match = re.search(r'\{(\d+(?:,\d+)*)\}', line)
        joltage = [int(x) for x in joltage_match.group(1).split(',')]

        machines.append({
            'diagram': diagram,
            'buttons': buttons,
            'joltage': joltage
        })
    return machines

def solve_gf2(target_vec, button_vecs):
    n = len(button_vecs)
    m = len(target_vec)

    matrix = []
    for i in range(m):
        row = [0] * (n + 1)
        for j in range(n):
            if i in button_vecs[j]:
                row[j] = 1
        row[n] = target_vec[i]
        matrix.append(row)

    pivot_row = 0
    pivot_cols = []
    for j in range(n):
        if pivot_row >= m:
            break
        for i in range(pivot_row, m):
            if matrix[i][j] == 1:
                matrix[pivot_row], matrix[i] = matrix[i], matrix[pivot_row]
                break
        else:
            continue

        pivot_cols.append(j)
        for i in range(m):
            if i != pivot_row and matrix[i][j] == 1:
                for k in range(j, n + 1):
                    matrix[i][k] ^= matrix[pivot_row][k]
        pivot_row += 1

    for i in range(pivot_row, m):
        if matrix[i][n] == 1:
            return None

    free_cols = [j for j in range(n) if j not in pivot_cols]
    min_weight = float('inf')
    num_free = len(free_cols)

    for bits in range(1 << num_free):
        x = [0] * n
        for i in range(num_free):
            if (bits >> i) & 1:
                x[free_cols[i]] = 1

        for i in range(pivot_row):
            p_col = -1
            for j in pivot_cols:
                if matrix[i][j] == 1:
                    p_col = j
                    break
            val = matrix[i][n]
            for f_col in free_cols:
                if matrix[i][f_col] == 1:
                    val ^= x[f_col]
            x[p_col] = val
        min_weight = min(min_weight, sum(x))

    return min_weight

def solve_linear_int(target_vec, button_vecs):
    n = len(button_vecs)
    m = len(target_vec)

    matrix = []
    for i in range(m):
        row = [Fraction(0)] * (n + 1)
        for j in range(n):
            if i in button_vecs[j]:
                row[j] = Fraction(1)
        row[n] = Fraction(target_vec[i])
        matrix.append(row)

    pivot_row = 0
    pivot_cols = []
    for j in range(n):
        if pivot_row >= m:
            break
        for i in range(pivot_row, m):
            if matrix[i][j] != 0:
                matrix[pivot_row], matrix[i] = matrix[i], matrix[pivot_row]
                break
        else:
            continue

        pivot_cols.append(j)
        pivot_val = matrix[pivot_row][j]
        for k in range(j, n + 1):
            matrix[pivot_row][k] /= pivot_val

        for i in range(m):
            if i != pivot_row:
                factor = matrix[i][j]
                if factor != 0:
                    for k in range(j, n + 1):
                        matrix[i][k] -= factor * matrix[pivot_row][k]
        pivot_row += 1

    for i in range(pivot_row, m):
        if matrix[i][n] != 0:
            return None

    free_cols = [j for j in range(n) if j not in pivot_cols]
    bounds = []
    for j in free_cols:
        b_max = 10**9
        if not button_vecs[j]:
            b_max = 0
        else:
            for i in button_vecs[j]:
                b_max = min(b_max, target_vec[i])
        bounds.append(b_max)

    min_total = float('inf')

    def search(idx, current_x_free):
        nonlocal min_total
        if idx == len(free_cols):
            x = [0] * n
            for k, f_col in enumerate(free_cols):
                x[f_col] = current_x_free[k]

            for i in range(pivot_row):
                p_col = pivot_cols[i]
                val = matrix[i][n]
                for k, f_col in enumerate(free_cols):
                    val -= matrix[i][f_col] * x[f_col]

                if val < 0 or val.denominator != 1:
                    return
                x[p_col] = int(val)

            min_total = min(min_total, sum(x))
            return

        for val in range(bounds[idx] + 1):
            # Pruning: check if pivot variables can still be non-negative
            possible = True
            for i in range(pivot_row):
                # x_p = d_i - sum_{j < idx} c_ij x_j - c_i_idx x_idx - sum_{j > idx} c_ij x_j
                # We don't know x_j for j > idx, but we know x_j >= 0.
                # So we can check if there's ANY combination of future x_j that makes x_p >= 0.
                pass # For now, just simple search

            current_x_free.append(val)
            search(idx + 1, current_x_free)
            current_x_free.pop()

    search(0, [])
    return min_total if min_total != float('inf') else None

def part_one(lines):
    machines = parse_machines(lines)
    total = 0
    for m in machines:
        target = [1 if c == '#' else 0 for c in m['diagram']]
        res = solve_gf2(target, m['buttons'])
        if res is not None:
            total += res
    return total

def part_two(lines):
    machines = parse_machines(lines)
    total = 0
    for m in machines:
        res = solve_linear_int(m['joltage'], m['buttons'])
        if res is not None:
            total += res
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

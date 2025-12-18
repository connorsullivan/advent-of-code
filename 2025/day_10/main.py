import sys
import os
import re
from collections import deque
from fractions import Fraction
from itertools import product

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _parse_machine(line: str) -> tuple[str, list[int], list[int]]:
    diagram = re.search(r"\[(.*?)\]", line).group(1)
    button_specs = [m.group(1) for m in re.finditer(r"\(([^)]*)\)", line)]
    buttons: list[int] = []
    for spec in button_specs:
        idxs = [int(x) for x in spec.split(",") if x.strip()]
        mask = 0
        for i in idxs:
            mask |= 1 << i
        buttons.append(mask)
    requirements = [int(x) for x in re.search(r"\{([^}]*)\}", line).group(1).split(",")]
    return diagram, buttons, requirements


def _rref(A: list[list[Fraction]], b: list[int]) -> tuple[list[list[Fraction]], list[int]]:
    m, n = len(A), len(A[0])
    aug = [row[:] + [Fraction(rhs)] for row, rhs in zip(A, b)]
    r = 0
    pivots: list[int] = []
    for c in range(n):
        pivot_row = None
        for rr in range(r, m):
            if aug[rr][c] != 0:
                pivot_row = rr
                break
        if pivot_row is None:
            continue
        aug[r], aug[pivot_row] = aug[pivot_row], aug[r]
        pv = aug[r][c]
        aug[r] = [v / pv for v in aug[r]]
        for rr in range(m):
            if rr != r and aug[rr][c] != 0:
                f = aug[rr][c]
                aug[rr] = [aug[rr][k] - f * aug[r][k] for k in range(n + 1)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return aug, pivots


def _min_presses_binary(target: int, button_masks: list[int], bits: int) -> int:
    dist = [-1] * (1 << bits)
    dist[0] = 0
    q: deque[int] = deque([0])
    while q:
        s = q.popleft()
        if s == target:
            return dist[s]
        nd = dist[s] + 1
        for m in button_masks:
            ns = s ^ m
            if dist[ns] == -1:
                dist[ns] = nd
                q.append(ns)
    raise ValueError("Unreachable target")


def _min_presses_additive(requirements: list[int], button_masks: list[int]) -> int:
    m = len(requirements)
    n = len(button_masks)
    A = [[0] * n for _ in range(m)]
    for j, mask in enumerate(button_masks):
        for i in range(m):
            if (mask >> i) & 1:
                A[i][j] = 1

    upper: list[int] = []
    for j in range(n):
        ub = min((requirements[i] for i in range(m) if A[i][j]), default=max(requirements))
        upper.append(ub)

    mat = [[Fraction(v) for v in row] for row in A]
    rr, pivots = _rref(mat, requirements)

    for row in rr:
        if all(v == 0 for v in row[:-1]) and row[-1] != 0:
            raise ValueError("Inconsistent machine definition")

    pivot_rows: dict[int, list[Fraction]] = {}
    for row in rr:
        pivot_col = None
        for c in pivots:
            if row[c] == 1:
                pivot_col = c
                break
        if pivot_col is not None:
            pivot_rows[pivot_col] = row

    free_cols = [c for c in range(n) if c not in pivots]
    if not free_cols:
        total = 0
        for pc in pivots:
            v = pivot_rows[pc][-1]
            if v.denominator != 1 or v.numerator < 0:
                raise ValueError("No nonnegative integer solution")
            total += int(v)
        return total

    best = None
    for free_vals in product(*(range(upper[c] + 1) for c in free_cols)):
        free = dict(zip(free_cols, free_vals, strict=True))
        sol = [0] * n
        ok = True
        for c, v in free.items():
            sol[c] = v

        for pc in pivots:
            row = pivot_rows[pc]
            v = row[-1]
            for fc, fv in free.items():
                if row[fc] != 0:
                    v -= row[fc] * fv
            if v.denominator != 1:
                ok = False
                break
            iv = int(v)
            if iv < 0:
                ok = False
                break
            sol[pc] = iv

        if not ok:
            continue
        total_presses = sum(sol)
        if best is None or total_presses < best:
            best = total_presses
    if best is None:
        raise ValueError("No solution found")
    return best


def part_one(lines):
    total = 0
    for line in lines:
        if not line:
            continue
        diagram, buttons, _ = _parse_machine(line)
        target = 0
        for i, ch in enumerate(diagram):
            if ch == "#":
                target |= 1 << i
        total += _min_presses_binary(target, buttons, len(diagram))
    return total

def part_two(lines):
    total = 0
    for line in lines:
        if not line:
            continue
        _, buttons, requirements = _parse_machine(line)
        total += _min_presses_additive(requirements, buttons)
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

import sys
import os
from functools import lru_cache

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _parse_graph(lines: list[str]) -> dict[str, list[str]]:
    g: dict[str, list[str]] = {}
    for line in lines:
        if not line:
            continue
        name, rest = line.split(":", 1)
        outs = [p for p in rest.strip().split() if p]
        g[name.strip()] = outs
    return g


def part_one(lines):
    g = _parse_graph(lines)

    visiting: set[str] = set()

    @lru_cache(maxsize=None)
    def count_paths(node: str) -> int:
        if node == "out":
            return 1
        if node in visiting:
            raise ValueError("Cycle detected on a reachable path")
        visiting.add(node)
        total = 0
        for nxt in g.get(node, []):
            total += count_paths(nxt)
        visiting.remove(node)
        return total

    return count_paths("you")

def part_two(lines):
    g = _parse_graph(lines)

    visiting: set[tuple[str, int]] = set()

    @lru_cache(maxsize=None)
    def count_paths(node: str, seen: int) -> int:
        if node == "dac":
            seen |= 1
        if node == "fft":
            seen |= 2
        if node == "out":
            return 1 if seen == 3 else 0
        state = (node, seen)
        if state in visiting:
            raise ValueError("Cycle detected on a reachable path")
        visiting.add(state)
        total = 0
        for nxt in g.get(node, []):
            total += count_paths(nxt, seen)
        visiting.remove(state)
        return total

    return count_paths("svr", 0)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

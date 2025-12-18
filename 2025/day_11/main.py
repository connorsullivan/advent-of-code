import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_graph(lines):
    """Parse the device connections into a graph."""
    graph = {}
    for line in lines:
        if not line or ':' not in line:
            continue
        parts = line.split(':')
        node = parts[0].strip()
        outputs = parts[1].strip().split()
        graph[node] = outputs
    return graph

def count_paths(graph, start, end, memo=None):
    """Count all paths from start to end using memoization."""
    if memo is None:
        memo = {}
    
    if start == end:
        return 1
    
    if start in memo:
        return memo[start]
    
    if start not in graph:
        return 0
    
    total = 0
    for next_node in graph[start]:
        total += count_paths(graph, next_node, end, memo)
    
    memo[start] = total
    return total

def count_paths_through(graph, start, end, via1, via2):
    """Count paths from start to end that pass through both via1 and via2."""
    # We need to find paths that visit both via1 and via2
    # The order can be: start -> via1 -> via2 -> end OR start -> via2 -> via1 -> end
    
    # Count paths: start -> via1 -> via2 -> end
    paths1 = count_paths(graph, start, via1, {}) * count_paths(graph, via1, via2, {}) * count_paths(graph, via2, end, {})
    
    # Count paths: start -> via2 -> via1 -> end
    paths2 = count_paths(graph, start, via2, {}) * count_paths(graph, via2, via1, {}) * count_paths(graph, via1, end, {})
    
    return paths1 + paths2

def part_one(lines):
    """Count paths from 'you' to 'out'."""
    graph = parse_graph(lines)
    return count_paths(graph, 'you', 'out', {})

def part_two(lines):
    """Count paths from 'svr' to 'out' that visit both 'dac' and 'fft'."""
    graph = parse_graph(lines)
    return count_paths_through(graph, 'svr', 'out', 'dac', 'fft')

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

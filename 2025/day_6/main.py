import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Solve math problems arranged vertically, reading left-to-right."""
    if not lines:
        return 0
    
    # Parse the grid
    grid = []
    for line in lines:
        grid.append(line)
    
    # Find columns (separated by all-space columns)
    max_len = max(len(line) for line in grid)
    
    # Identify problem boundaries
    problems = []
    current_problem = []
    
    for col in range(max_len):
        # Check if this column is all spaces (separator)
        is_separator = True
        for row in range(len(grid)):
            if col < len(grid[row]) and grid[row][col] != ' ':
                is_separator = False
                break
        
        if is_separator:
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)
    
    # Don't forget the last problem
    if current_problem:
        problems.append(current_problem)
    
    # Solve each problem
    grand_total = 0
    for problem_cols in problems:
        # Extract numbers and operator from this problem
        numbers = []
        operator = None
        
        for row in range(len(grid)):
            # Collect digits from this row for this problem
            num_str = ''
            for col in problem_cols:
                if col < len(grid[row]):
                    char = grid[row][col]
                    num_str += char
            
            num_str = num_str.strip()
            if num_str:
                if num_str in ['+', '*']:
                    operator = num_str
                elif num_str.isdigit():
                    numbers.append(int(num_str))
        
        # Calculate result
        if operator and numbers:
            result = numbers[0]
            for num in numbers[1:]:
                if operator == '+':
                    result += num
                else:  # *
                    result *= num
            grand_total += result
    
    return grand_total

def part_two(lines):
    """Solve math problems reading right-to-left in columns."""
    if not lines:
        return 0
    
    grid = lines
    max_len = max(len(line) for line in grid)
    
    # Identify problem boundaries (columns separated by all-space columns)
    problems = []
    current_problem = []
    
    for col in range(max_len):
        # Check if this column is all spaces (separator)
        is_separator = True
        for row in range(len(grid)):
            if col < len(grid[row]) and grid[row][col] != ' ':
                is_separator = False
                break
        
        if is_separator:
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)
    
    if current_problem:
        problems.append(current_problem)
    
    # Solve each problem reading RIGHT-TO-LEFT, column by column
    grand_total = 0
    for problem_cols in problems:
        numbers = []
        operator = None
        
        # Process EACH single-character column from right to left
        for col in reversed(problem_cols):
            # Read this single column top-to-bottom
            col_chars = []
            for row in range(len(grid)):
                if col < len(grid[row]):
                    col_chars.append(grid[row][col])
            
            # Build a number or find operator from this column
            col_str = ''.join(col_chars).strip()
            
            # Check if it contains an operator
            if '+' in col_str:
                operator = '+'
                # Also extract the number part
                num_str = col_str.replace('+', '').replace(' ', '')
                if num_str and num_str.isdigit():
                    numbers.append(int(num_str))
            elif '*' in col_str:
                operator = '*'
                # Also extract the number part
                num_str = col_str.replace('*', '').replace(' ', '')
                if num_str and num_str.isdigit():
                    numbers.append(int(num_str))
            elif col_str and col_str.replace(' ', '').isdigit():
                # It's a number - remove spaces and convert
                num_str = col_str.replace(' ', '')
                if num_str:
                    numbers.append(int(num_str))
        
        # Calculate result
        if operator and numbers:
            result = numbers[0]
            for num in numbers[1:]:
                if operator == '+':
                    result += num
                else:  # *
                    result *= num
            grand_total += result
    
    return grand_total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

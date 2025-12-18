import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_worksheet(lines):
    """Parse the worksheet into columns of problems."""
    if not lines:
        return []
    
    # Find max width
    max_width = max(len(line) for line in lines)
    
    # Pad all lines to same width
    padded = [line.ljust(max_width) for line in lines]
    
    # Transpose to get columns
    cols = []
    for c in range(max_width):
        col = ''.join(row[c] if c < len(row) else ' ' for row in padded)
        cols.append(col)
    
    return cols, padded

def part_one(lines):
    """Solve problems reading left to right, numbers vertically."""
    if not lines:
        return 0
    
    # Last line is the operators
    operator_line = lines[-1]
    data_lines = lines[:-1]
    
    # Find the max width
    max_width = max(len(line) for line in lines)
    
    # Pad all lines
    padded_data = [line.ljust(max_width) for line in data_lines]
    operator_padded = operator_line.ljust(max_width)
    
    # Parse problems - problems are separated by columns of spaces
    problems = []
    current_numbers = []
    current_op = None
    current_start = 0
    
    c = 0
    while c < max_width:
        # Check if this column is a separator (all spaces in data rows)
        is_separator = all(line[c] == ' ' for line in padded_data)
        
        if is_separator:
            # End current problem if we have one
            if current_numbers or current_op is not None:
                problems.append((current_numbers, current_op))
                current_numbers = []
                current_op = None
            c += 1
        else:
            # Read a number token (spans until next space column or end)
            token_chars = []
            while c < max_width and not all(line[c] == ' ' for line in padded_data):
                for row in padded_data:
                    if row[c] not in ' ':
                        token_chars.append((c, row[c]))
                        break
                # Get operator for this column
                if c < len(operator_padded) and operator_padded[c] in '+*':
                    current_op = operator_padded[c]
                c += 1
    
    if current_numbers or current_op is not None:
        problems.append((current_numbers, current_op))
    
    # Actually, let's re-parse more carefully
    # Each column either has a digit or spaces in data rows
    # Columns of all spaces separate problems
    
    max_width = max(len(line) for line in lines)
    padded_data = [line.ljust(max_width) for line in data_lines]
    operator_padded = operator_line.ljust(max_width)
    
    # Group columns into problems
    problems = []
    current_cols = []
    
    for c in range(max_width):
        is_separator = all(line[c] == ' ' for line in padded_data)
        if is_separator:
            if current_cols:
                problems.append(current_cols)
                current_cols = []
        else:
            current_cols.append(c)
    
    if current_cols:
        problems.append(current_cols)
    
    # For each problem, extract numbers and operator
    total = 0
    for cols in problems:
        # Get operator from last line
        op = None
        for c in cols:
            if c < len(operator_padded) and operator_padded[c] in '+*':
                op = operator_padded[c]
                break
        
        # Get numbers - each data row contributes one number
        numbers = []
        for row in padded_data:
            num_str = ''.join(row[c] for c in cols).strip()
            if num_str:
                numbers.append(int(num_str))
        
        if op == '+':
            result = sum(numbers)
        else:  # *
            result = 1
            for n in numbers:
                result *= n
        
        total += result
    
    return total

def part_two(lines):
    """Solve problems reading right to left, numbers in columns."""
    if not lines:
        return 0
    
    # Last line is the operators
    operator_line = lines[-1]
    data_lines = lines[:-1]
    
    max_width = max(len(line) for line in lines)
    padded_data = [line.ljust(max_width) for line in data_lines]
    operator_padded = operator_line.ljust(max_width)
    
    # Group columns into problems
    problems = []
    current_cols = []
    
    for c in range(max_width):
        is_separator = all(line[c] == ' ' for line in padded_data)
        if is_separator:
            if current_cols:
                problems.append(current_cols)
                current_cols = []
        else:
            current_cols.append(c)
    
    if current_cols:
        problems.append(current_cols)
    
    # For each problem, read numbers vertically from columns (right to left)
    total = 0
    for cols in problems:
        # Get operator
        op = None
        for c in cols:
            if c < len(operator_padded) and operator_padded[c] in '+*':
                op = operator_padded[c]
                break
        
        # Read numbers vertically: each column is a number, top to bottom is most to least significant
        numbers = []
        for c in reversed(cols):  # Right to left
            num_chars = []
            for row in padded_data:
                if row[c] not in ' ':
                    num_chars.append(row[c])
            if num_chars:
                numbers.append(int(''.join(num_chars)))
        
        if op == '+':
            result = sum(numbers)
        else:  # *
            result = 1
            for n in numbers:
                result *= n
        
        total += result
    
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")

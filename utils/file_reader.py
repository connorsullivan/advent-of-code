import os

def read_input(file_path):
    """Reads the input file and returns a list of lines stripped of whitespace."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def read_input_raw(file_path):
    """Reads the input file and returns the raw content."""
    if not os.path.exists(file_path):
        return ""

    with open(file_path, 'r') as f:
        return f.read()

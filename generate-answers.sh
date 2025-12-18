#!/bin/bash

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if year argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./generate-answers.sh <year>"
    exit 1
fi

YEAR=$1
YEAR_DIR="./$YEAR"
ANSWERS_FILE="./answers.yml"

# Check if year directory exists
if [ ! -d "$YEAR_DIR" ]; then
    echo "Error: Directory $YEAR_DIR not found"
    exit 1
fi

echo ""
echo "=========================================="
echo "Generating answers for year: $YEAR"
echo "=========================================="
echo ""

# Temporary file to store results before merging into YAML
RESULTS_FILE="./.results.tmp"
touch "$RESULTS_FILE"

# Iterate through day directories in numeric order
for day_dir in $(find "$YEAR_DIR" -maxdepth 1 -type d -name 'day_*' | sort -V); do
    if [ -d "$day_dir" ]; then
        day_name=$(basename "$day_dir")
        main_py="$day_dir/main.py"

        if [ ! -f "$main_py" ]; then
            continue
        fi

        echo "Processing $day_name..."

        # Run main.py and capture output
        cd "$day_dir"
        output=$(python main.py 2>&1)
        cd - > /dev/null

        # Parse Part One and Part Two from output
        part_one=$(echo "$output" | grep "^Part One:" | sed 's/Part One: //')
        part_two=$(echo "$output" | grep "^Part Two:" | sed 's/Part Two: //')

        # Store in temp file: day_name|part_1|part_2
        echo "$day_name|$part_one|$part_two" >> "$RESULTS_FILE"
    fi
done

# Use Python to update/create answers.yml
python << EOF
import yaml
import os

answers_file = '$ANSWERS_FILE'
year = '$YEAR'
results_file = '$RESULTS_FILE'

# Load existing data if file exists
data = {}
if os.path.exists(answers_file):
    try:
        with open(answers_file, 'r') as f:
            data = yaml.safe_load(f) or {}
    except Exception as e:
        print(f"Warning: Could not read existing {answers_file}: {e}")

# Ensure year key exists (handle both int and str)
year_key = year
if year not in data:
    try:
        if int(year) in data:
            year_key = int(year)
    except ValueError:
        pass

if year_key not in data:
    data[year_key] = {}

# Read results and update data
with open(results_file, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split('|')
        if len(parts) < 3:
            continue
        day, p1, p2 = parts[0], parts[1], parts[2]

        if day not in data[year_key]:
            data[year_key][day] = {}

        if p1:
            data[year_key][day]['part_1'] = p1
        if p2:
            data[year_key][day]['part_2'] = p2

# Write back to YAML
with open(answers_file, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False)

print(f"\nSuccessfully updated {answers_file} for year {year}")
EOF

# Clean up
rm "$RESULTS_FILE"

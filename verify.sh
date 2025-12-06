#!/bin/bash

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if year argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./verify.sh <year>"
    exit 1
fi

YEAR=$1
YEAR_DIR="./$YEAR"
ANSWERS_FILE="./answers.yml"

# Check if answers file exists
if [ ! -f "$ANSWERS_FILE" ]; then
    echo "Error: answers.yml file not found in the root directory"
    exit 1
fi

# Check if year directory exists
if [ ! -d "$YEAR_DIR" ]; then
    echo "Error: Directory $YEAR_DIR not found"
    exit 1
fi

# Initialize counters
PASSED=0
FAILED=0

echo ""
echo "=========================================="
echo "Running verification for year: $YEAR"
echo "=========================================="
echo ""

# Function to parse YAML value
parse_yaml() {
    local file=$1
    local key=$2
    grep "^\s*$key:" "$file" | sed 's/.*: //' | tr -d '"' | tr -d "'"
}

# Function to get day answers from YAML
get_day_answer() {
    local day=$1
    local part=$2
    local year=$3

    # Use Python for reliable YAML parsing
    python << EOF
import yaml
try:
    with open('$ANSWERS_FILE', 'r') as f:
        data = yaml.safe_load(f)
        # Try both string and integer year keys since YAML might parse as int
        year_data = data.get($year, {}) or data.get('$year', {})
        day_data = year_data.get('$day', {})
        answer = day_data.get('$part', '')
        print(answer if answer is not None else '')
except Exception as e:
    print('')
EOF
}

# Iterate through day directories in numeric order
for day_dir in $(find "$YEAR_DIR" -maxdepth 1 -type d -name 'day_*' | sort -V); do
    if [ -d "$day_dir" ]; then
        day_name=$(basename "$day_dir")
        main_py="$day_dir/main.py"

        if [ ! -f "$main_py" ]; then
            continue
        fi

        # Run main.py and capture output
        cd "$day_dir"
        output=$(python main.py 2>&1)
        cd - > /dev/null

        # Parse Part One and Part Two from output
        part_one=$(echo "$output" | grep "^Part One:" | sed 's/Part One: //')
        part_two=$(echo "$output" | grep "^Part Two:" | sed 's/Part Two: //')

        # Get expected answers
        expected_one=$(get_day_answer "$day_name" "part_1" "$YEAR")
        expected_two=$(get_day_answer "$day_name" "part_2" "$YEAR")

        # Extract day number and format for display
        day_num=$(echo "$day_name" | sed 's/day_//')
        echo "Day $day_num:"

        # Compare Part One
        if [ -z "$expected_one" ]; then
            echo "  Part 1: ⊘ (no expected answer)"
        elif [ "$part_one" = "$expected_one" ]; then
            echo -e "  Part 1: ${GREEN}✓${NC}"
            ((PASSED++))
        else
            echo -e "  Part 1: ${RED}✗${NC}"
            echo "    expected: $expected_one"
            echo "    got:      $part_one"
            ((FAILED++))
        fi

        # Compare Part Two
        if [ -z "$expected_two" ]; then
            echo "  Part 2: ⊘ (no expected answer)"
        elif [ "$part_two" = "$expected_two" ]; then
            echo -e "  Part 2: ${GREEN}✓${NC}"
            ((PASSED++))
        else
            echo -e "  Part 2: ${RED}✗${NC}"
            echo "    expected: $expected_two"
            echo "    got:      $part_two"
            ((FAILED++))
        fi

        echo ""
    fi
done

# Print summary
echo "=========================================="
echo "Summary:"
echo -e "  Passed: ${GREEN}$PASSED${NC}"
echo -e "  Failed: ${RED}$FAILED${NC}"
echo "=========================================="

# Exit with appropriate code
if [ $FAILED -eq 0 ]; then
    exit 0
else
    exit 1
fi

# Day 3: Mull It Over

## Part 1
The problem requires scanning a corrupted memory string for valid multiplication instructions in the format `mul(X,Y)`, where X and Y are 1-3 digit numbers.

### Approach
I used Python's `re` module to find all occurrences of the pattern `mul\((\d{1,3}),(\d{1,3})\)`.
- The regex captures the two numbers.
- I iterated through all matches, converted the captured strings to integers, multiplied them, and summed the results.

## Part 2
The second part introduces conditional statements `do()` and `don't()` that enable or disable future multiplication instructions.

### Approach
I extended the regex to capture `do()` and `don't()` instructions as well:
`r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"`

- I iterated through the matches in order.
- I maintained a boolean flag `enabled`, initialized to `True`.
- If `do()` is encountered, `enabled` is set to `True`.
- If `don't()` is encountered, `enabled` is set to `False`.
- If a `mul` instruction is encountered, the multiplication is performed and added to the total only if `enabled` is `True`.

## Complexity
- **Time Complexity**: O(N), where N is the length of the input string. The regex engine scans the string linearly.
- **Space Complexity**: O(M), where M is the number of matches found. The `re.findall` function returns a list of all matches.

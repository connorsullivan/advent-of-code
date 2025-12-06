# Day 5: Print Queue

## Part 1
The problem asks us to validate the order of pages in several updates based on a set of ordering rules `X|Y` (page X must be printed before page Y).

### Approach
1.  **Parsing**: The input is split into two sections: rules and updates.
    *   Rules are parsed into a set of tuples `(X, Y)` for O(1) lookup.
    *   Updates are parsed into lists of integers.
2.  **Validation**: For each update, we check if it satisfies the rules.
    *   Instead of checking all rules against the update, we iterate through every pair of pages `(page_i, page_j)` in the update where `i < j`.
    *   If there exists a rule `page_j|page_i` (meaning `page_j` must come before `page_i`), the update is invalid because `page_j` appears after `page_i`.
3.  **Calculation**: For valid updates, we find the middle page number and sum them up.

### Complexity
*   **Time**: O(U * K^2), where U is the number of updates and K is the average number of pages per update. Looking up rules in the set is O(1).
*   **Space**: O(R), where R is the number of rules, to store the rules set.

## Part 2
The second part asks us to correct the order of the invalid updates and then sum their middle page numbers.

### Approach
1.  **Identification**: We identify updates that failed the validation in Part 1.
2.  **Sorting**: The rules define a partial ordering. We can sort the pages in an update using a custom comparison function.
    *   `compare(a, b)` returns -1 if `a|b` is a rule (a < b).
    *   `compare(a, b)` returns 1 if `b|a` is a rule (b < a).
    *   Otherwise 0.
    *   We use Python's `sorted` with `functools.cmp_to_key` to apply this custom comparator.
3.  **Calculation**: For the newly sorted updates, we find the middle page number and sum them up.

### Complexity
*   **Time**: O(U_invalid * K log K), where U_invalid is the number of invalid updates. Sorting takes O(K log K).
*   **Space**: O(R) for the rules set.

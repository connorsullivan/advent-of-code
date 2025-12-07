# Day 5: Print Queue

## Problem Summary
The problem involves validating and sorting page updates according to ordering rules. Rules are specified as `X|Y` meaning page X must come before page Y if both are present in an update.

## Part One: Validate Correctly Ordered Updates

**Approach:**
1. Parse input into two sections: ordering rules and page updates
2. For each update, check if it satisfies all applicable rules
3. A rule `X|Y` only applies if both X and Y are in the update
4. Sum the middle page numbers of all correctly ordered updates

**Implementation:**
- Create a position map for each update to quickly look up page positions
- For each rule, check if both pages exist and if X comes before Y
- If all applicable rules are satisfied, the update is valid
- Extract middle element (at index `len(update) // 2`)

**Answer: 7024**

## Part Two: Fix Incorrectly Ordered Updates

**Approach:**
1. Identify updates that violate ordering rules
2. Sort these updates according to the rules
3. Sum the middle page numbers of the corrected updates

**Implementation:**
- Use a custom comparison function that checks the ordering rules
- For pages A and B, return -1 if rule `A|B` exists (A before B)
- Return 1 if rule `B|A` exists (B before A)
- Use `functools.cmp_to_key` to convert the comparison function for sorting
- This creates a topological ordering respecting all rules

**Key Insight:**
The ordering rules define a partial order on the pages. For any update, we can use the rules as a comparison function to sort the pages into the correct order. The comparison function needs to check if there's a direct rule between two pages to determine their relative ordering.

**Answer: 4151**

## Complexity
- **Time:** O(n × m × r) where n is number of updates, m is average update length, r is number of rules
- **Space:** O(m) for position maps and sorted lists

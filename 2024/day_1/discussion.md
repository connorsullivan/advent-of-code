# Day 1 - Historian Hysteria

## Part One: Total Distance Between Lists

The problem requires us to calculate the total distance between two lists of location IDs.

**Approach:**
1. Parse the input to extract two separate lists (left and right columns)
2. Sort both lists in ascending order
3. Pair up corresponding elements from both sorted lists (smallest with smallest, etc.)
4. Calculate the absolute difference for each pair
5. Sum all the differences to get the total distance

**Implementation Details:**
- Split each line on whitespace to get the two numbers
- Use Python's built-in `sort()` for efficiency (O(n log n))
- Zip the sorted lists together for easy pairing
- Use `abs()` to get the absolute difference between each pair

**Result:** 936063

## Part Two: Similarity Score

The second part asks us to calculate a "similarity score" based on how often numbers from the left list appear in the right list.

**Approach:**
1. Parse the input to extract both lists (same as Part One)
2. Create a frequency map (dictionary) counting occurrences of each number in the right list
3. For each number in the left list, multiply it by its count in the right list
4. Sum all these products to get the similarity score

**Implementation Details:**
- Use a dictionary to count occurrences in the right list (O(n) time)
- For each left number, look up its count in the dictionary (O(1) per lookup)
- If a number doesn't exist in the right list, its count is 0, contributing 0 to the score
- Overall time complexity: O(n) where n is the length of the lists

**Result:** 23150395

## Key Insights

- Part One is a classic sorting and matching problem
- Part Two demonstrates the usefulness of frequency counting with hash maps
- Both parts require parsing the same input format but use different algorithms
- The similarity score naturally handles numbers that don't appear in both lists (multiplying by 0)

# Day 5

## Part One
Split the input on the blank line into the fresh ID ranges and the list of available IDs. Merge overlapping ranges, then count how many available IDs fall into any merged interval using binary search membership checks.

## Part Two
The available ID list is irrelevant; only the merged ranges matter. The number of fresh IDs is the sum of the lengths of all merged intervals, computed as `end - start + 1` for each.

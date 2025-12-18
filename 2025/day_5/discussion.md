# Day 5

## Part One

The first section lists inclusive “fresh” ID ranges; the second section lists available IDs.
Overlapping ranges are allowed, so we first merge them into disjoint, sorted intervals.

Then for each available ID, we binary-search the merged interval list to test membership and count the fresh ones.

## Part Two

The available-ID section is ignored; we just need how many integers are covered by the union of ranges.
After merging into disjoint intervals, the count is:

`sum(end - start + 1)`

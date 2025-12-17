# Day 4

## Part One
The problem asks us to count the number of paper rolls (`@`) that are "accessible". A roll is accessible if it has fewer than four rolls in its eight adjacent positions (horizontal, vertical, and diagonal).

I implemented this by:
1. Parsing the input into a set of coordinates for all paper rolls.
2. Iterating through each roll and checking its 8 neighbors.
3. Counting how many of those neighbors are also in the set of rolls.
4. If the count is less than 4, the roll is accessible.

## Part Two
Part Two introduces a simulation where accessible rolls are removed, which can make other rolls accessible. We need to find the total number of rolls that can be removed.

I used a "wave-based" approach to optimize the simulation:
1. Start with the set of all rolls.
2. In the first wave, check all rolls to see which are accessible.
3. For each subsequent wave, only check the neighbors of the rolls that were removed in the previous wave, as these are the only ones whose neighbor count could have changed.
4. Continue until no more rolls are removed in a wave.
5. The total number of removed rolls is the sum of rolls removed in all waves.

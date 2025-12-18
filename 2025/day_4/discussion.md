# Day 4

## Part One
Convert the map to a boolean grid and precompute, for each roll, how many neighboring cells in the 8 directions also contain rolls. A roll is accessible when this count is below four; count them directly from the initial grid.

## Part Two
Treat removal as peeling a graph with a degree threshold. Start by enqueueing all rolls whose neighbor count is below four. Repeatedly remove a roll, decrement neighbor counts of adjacent rolls, and enqueue any that newly fall below the threshold. The total number of removed rolls is the answer.

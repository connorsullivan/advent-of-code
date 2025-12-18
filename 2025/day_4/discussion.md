# Day 4

## Part One

Count paper rolls that can be accessed by the forklift (fewer than 4 adjacent neighbors). We iterate through the grid and count '@' cells with fewer than 4 neighboring '@' cells.

## Part Two

Repeatedly remove accessible rolls until no more can be removed. In each iteration, we find all rolls with fewer than 4 neighbors and remove them all, then repeat until no rolls can be removed.

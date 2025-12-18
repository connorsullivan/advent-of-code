# Day 9

## Part One

The rectangle is axis-aligned and uses inclusive grid coordinates, so the area is:

`(|x1 - x2| + 1) * (|y1 - y2| + 1)`

With only 496 red tiles, brute-forcing all pairs is fast enough (`~123k` pairs).

## Part Two

The red tiles are given in loop order, and consecutive points share a row or column, so they define an orthogonal simple polygon.
Green tiles are the polygon’s boundary segments and filled interior.

For any candidate rectangle (picked by two red opposite corners), we require the entire rectangle to be inside the polygon.
The chosen red corners are already on the boundary, so the only non-trivial checks are:

- the other two rectangle corners are inside/on the polygon (ray casting against vertical edges, with boundary treated as inside)
- the polygon boundary does not cross the open interior of the rectangle (quick segment-vs-open-rectangle intersection test)

Degenerate “thin rectangles” (width 1 or height 1) are handled by checking the midpoint is inside and that no boundary edge crosses the open segment.

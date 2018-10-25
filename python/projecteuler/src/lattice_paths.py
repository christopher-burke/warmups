#!/usr/bin/env python3

"""Lattice paths.

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

source: https://projecteuler.net/problem=15
"""


def _lattice_path(down, right):
    """Lattice path helper function."""
    if down == 0 or right == 0:
        return 1
    else:
        return _lattice_path(down - 1, right) + _lattice_path(down, right - 1)


def lattice_paths(grid_size):
    """Brute force recursive function to get total lattice paths.

    :return: The number of lattice paths.
    """
    return _lattice_path(int(grid_size), int(grid_size))


def main(grid_size):
    """Run Lattice paths."""
    return lattice_paths(grid_size)


if __name__ == "__main__":
    print(main(grid_size=4))

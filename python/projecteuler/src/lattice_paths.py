#!/usr/bin/env python3

"""Lattice paths.

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

source: https://projecteuler.net/problem=15
"""


import math


def _lattice_path(down, right):
    """Shortest paths using binomial coefficients.

    Binomial[2n, n] or  (2n)!/(n!)^2

    More info can be found here:
      * https://www.robertdickau.com/manhattan.html

    :return:  Number of paths.
    """
    return math.factorial(down + right) // (math.factorial(down) ** 2)


def lattice_paths(grid_size):
    """Brute force recursive function to get total lattice paths.

    :return: The number of lattice paths.
    """
    return _lattice_path(int(grid_size), int(grid_size))


def main(grid_size):
    """Run Lattice paths."""
    return lattice_paths(grid_size)


if __name__ == "__main__":
    print(main(grid_size=20))

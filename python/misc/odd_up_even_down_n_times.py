#!/usr/bin/env python3

"""Odd Up, Even Down - N Times.

Create a function that performs an even-odd transform to a list, n times.

Each even-odd transformation:

Adds two (+2) to each odd integer.
Subtracts two (-2) to each even integer.

Source:
https://edabit.com/challenge/ke4FSMdG2XYxbGQny
"""

from typing import List


def logic(number: int) -> int:
    """Perform logic for even-odd transformation.

    Each even-odd transformation:
        * Adds two (+2) to each odd integer.
        * Subtracts two (-2) to each even integer.
    """
    # Determine the modifier based on number being even or odd.
    modifier = -2 if number % 2 == 0 else 2
    return number + modifier


def odd_even_transform(lst: List, n: int) -> List:
    """Perform an even-odd transform to a list, n times.

    Uses logic function to perform transformation.
    """
    for _ in range(n):
        lst = [logic(item) for item in lst]

    return lst


def main():
    """Run sample odd_even_transform functions. Do not import."""
    # Run assert statments to test odd_even_transform.
    assert odd_even_transform([3, 4, 9], 3) == [9, -2, 15]
    assert odd_even_transform([0, 0, 0], 10) == [-20, -20, -20]
    assert odd_even_transform([1, 2, 3], 1) == [3, 0, 5]
    assert odd_even_transform([55, 90, 830], 2) == [59, 86, 826]
    print("Passed.")


if __name__ == "__main__":
    main()

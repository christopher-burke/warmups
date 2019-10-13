#!/usr/bin/env python3

"""The Farm Problem.

You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
Return the total number of legs on your farm.

Source:
https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT
"""


def animals(chickens: int, cows: int, pigs: int) -> int:
    """Return the total number of legs on your farm."""
    return sum([(chickens * 2), (cows * 4), (pigs * 4), ])


def main():
    """Run sample animals functions. Do not import."""
    assert animals(5, 2, 8) == 50
    assert animals(3, 4, 7) == 50
    assert animals(1, 2, 3) == 22
    assert animals(3, 5, 2) == 34


if __name__ == "__main__":
    main()

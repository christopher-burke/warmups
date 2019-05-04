#!/usr/bin/env python3

"""Multiply by Length.

Create a function to multiply all values in a list by the amount of
items contained in that list.

Source:
https://edabit.com/challenge/2kz9W4tqZyCNCAhik
"""


def multiply_by_length(items):
    """Multiply all values by length of list.

    Arguments:
        items {list} -- list of numbers

    Returns:
        list -- items multiplied by length of items.

    """
    return [x * len(items) for x in items]


def main():
    """Run sample multiply_by_length functions."""
    print(multiply_by_length([2, 3, 1, 0]))
    print(multiply_by_length([4, 1, 1]))
    print(multiply_by_length([1, 0, 3, 3, 7, 2, 1]))
    print(multiply_by_length([0]))


if __name__ == "__main__":
    main()

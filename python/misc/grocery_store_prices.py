#!/usr/bin/env python3

"""Grocery Store Prices.

You are given a list of strings consisting of grocery items,
with prices in parentheses. Return a list of prices in float format.

Source:
https://edabit.com/challenge/tQPApXhwoQ6zztxWJ
"""

import re


def get_prices(lst: list) -> list:
    """Return a list of prices in float format."""
    return [float(item)
            for item in re.findall(r"(\d+\.\d+)", "".join(lst))]


def main():
    """Run sample functions. Do not import."""
    assert get_prices([
        'ice cream ($5.99)',
        'banana ($0.20)',
        'sandwich ($8.50)',
        'soup ($1.99)',
    ]) == [5.99, 0.2, 8.50, 1.99]
    assert get_prices([
        'salad ($4.99)',
    ]) == [4.99]
    assert get_prices([
        'artichokes ($1.99)',
        'rotiserrie chicken ($5.99)',
        'gum ($0.75)',
    ]) == [1.99, 5.99, 0.75]
    assert get_prices([
        'pizza ($2.99)',
        'shampoo ($15.75)',
        'trash bags ($15.00)'
    ]) == [2.99, 15.75, 15]
    print('Passed.')


if __name__ == "__main__":
    main()

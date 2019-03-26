#!/usr/bin/env python3

"""Accumulating Product.

Create a function that takes a list and returns a
list of the accumulating product.

"""

from functools import reduce
from itertools import accumulate
from operator import mul


def accumulating_product_reduce(items):
    """Calculate the accumulating product of a list.

    Uses functools.reduce.

    Arguments:
        items {[list]} -- List of numbers.

    Returns:
        [list] -- List of accumulating products.

    """
    return [reduce(mul, items[:i+1]) for i in range(len(items))]


def accumulating_product_acc(items):
    """Calculate the accumulating product of a list.

    Uses itertools.accumulate.

    Arguments:
        items {[list]} -- List of numbers.

    Returns:
        [list] -- List of accumulating products.

    """
    return list(accumulate(items, func=mul))


def accumulating_product(items, func=accumulating_product_acc):
    """Calculate the accumulating product of a list.

    Arguments:
        items {[list]} -- List of numbers.

    Keyword Arguments:
        func {[function]} -- Use the reduce or acc functions in this module. 0
        (default: {accumulating_product_acc})

    Returns:
        [function] -- Results from the func call.

    """
    return func(items)


def main():
    """Run sample accumulating_product functions."""
    print(accumulating_product([1, 2, 3, 4]))
    print(accumulating_product([1, 2, 3, 4]))
    print(accumulating_product([1, 5, 7]))
    print(accumulating_product([1, 0, 1, 0]))
    print(accumulating_product([]))


if __name__ == "__main__":
    main()

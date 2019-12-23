#!/usr/bin/env python3


"""Sort Numbers in Descending Order.

Create a function that takes any non-negative number as an argument and
returns it with its digits in descending order. Descending order is when
you sort from highest to lowest.

Source:
https://edabit.com/challenge/B7rfWiJKrwft9yXXC
"""


def sort_decending(num):
    """Sort in descending order."""
    return int("".join(sorted([n for n in str(num)], reverse=True)))


def main():
    """Run sample sort_decending functions. Do not import."""
    assert sort_decending(123) == 321
    assert sort_decending(670276097) == 977766200
    assert sort_decending(2619805) == 9865210
    assert sort_decending(81294) == 98421
    assert sort_decending(0000000) == 0000000
    assert sort_decending(321) == 321
    assert sort_decending(628904) == 986420
    assert sort_decending(289327560) == 987653220
    assert sort_decending(6456) == 6654
    assert sort_decending(444111888555333) == 888555444333111
    print('Passed.')


if __name__ == "__main__":
    main()

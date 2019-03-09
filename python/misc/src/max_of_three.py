#!/usr/bin/env python3

"""Max Of Three.

Implement a function that takes as input three variables, and returns the
largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals
that Python normally takes care of for us.
All you need is some variables and if statements!

Source:
https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
"""


def find_max(items: list):
    """From a list of items, return the max."""
    max_ = None
    for x in items:
        if not max_:
            max_ = x
            continue
        if max_ < x:
            max_ = x
    return max_


def main():
    """Max of three samples."""
    print(find_max([100, 200, 3, ]))
    print(find_max([117, 27, 37, ]))


if __name__ == "__main__":
    main()

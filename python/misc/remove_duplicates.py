#!/usr/bin/env python3

"""Remove Duplicates.

Source: https://practice.geeksforgeeks.org/problems/remove-duplicates/0
"""

from collections import OrderedDict


def remove_duplicates(text: str) -> str:
    """Remove duplicates from text.

    Function uses OrderedDict, which keeps order and distinct elements.
    """
    set_ = OrderedDict()
    for x in text:
        set_[x] = None

    return ''.join(set_.keys())


def main():
    remove_duplicates('geeksforgeeks')
    remove_duplicates('geeks for geeks')


if __name__ == "__main__":
    main()

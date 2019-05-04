#!/usr/bin/env python3

"""Zig Zag.
Given an array A (distinct elements) of size N.
Rearrange the elements of array in zig-zag fashion.
The converted array should be in form a < b > c < d > e < f.
The relative order of elements is same in the output
i.e you have to iterate on the original array only.

Source:
https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion/0
"""


def zig_zag(items: list) ->list:
    """Rearrange the elements of a list in zig-zag fashion.

    Changes to the list are made in place.
    """
    less_than = True
    for i in range(len(items)-1):
        if (less_than) and items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]
        else:
            if items[i] < items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
        less_than = bool(1 - less_than)
    return items


def zig_zag_both(items: list) -> tuple:
    """Return original and zig-zap lists in a tuple."""
    return (items[:], zig_zag(items),)


def main():
    """Main function to run zig-zag functions."""
    print(zig_zag([4, 3, 7, 8, 6, 2, 1, ]))
    print(zig_zag([1, 4, 3, 2, ]))
    print(zig_zag_both([4, 3, 7, 8, 6, 2, 1, ]))
    print(zig_zag_both([1, 4, 3, 2, ]))


if __name__ == "__main__":
    main()

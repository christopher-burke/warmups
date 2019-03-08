#!/usr/bin/env python3

"""Find the element that appears once in sorted array.

Given a sorted array A, size N, of integers; every element appears twice except for one. Find that element 
in linear time complexity and without using extra memory.

Source:
https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array/0
"""


def find_unique_value(items: list):
    """Find the element that appears once in sorted array."""
    unique = -1
    for index, i in enumerate(items):
        # Set the unique value. Continue to next i value.
        if unique < 0:
            unique = i
            continue
        # If duplicate found and next is different, reset to -1.
        if unique == i and i != items[index + 1]:
            unique = -1
        # Since list is sorted, once unique is greater than 0
        # and i is less than unique break from loop.
        if unique > 0 and unique < i:
            break
    return unique


def main():
    print(find_unique_value(
        items=[1, 1, 1, 2, 2, 2, 3, 3, 4, 50, 50, 65, 65, ]))


if __name__ == "__main__":
    main()

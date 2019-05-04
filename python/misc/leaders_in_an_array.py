#!/usr/bin/env python3

"""Leaders in an array.


Given an array of positive integers. Your task is to find the leaders in the array.

Note: An element of array is leader if it is greater than or equal to all the elements to its right side. 
Also, the rightmost element is always a leader. 
"""

from itertools import compress


def find_leaders(A):
    """Find all the leaders in an array."""
    leaders = []

    for index, item in enumerate(A):
        leaders.append(len(A[index+1:]) ==
                       len(tuple(filter(lambda x: x <= item, A[index+1:]))))

    return tuple(compress(A, leaders))


if __name__ == "__main__":
    print(find_leaders((16, 17, 4, 3, 5, 2,)))
    print(find_leaders((1, 2, 3, 4, 0,)))
    print(find_leaders((7, 4, 5, 7, 3,)))

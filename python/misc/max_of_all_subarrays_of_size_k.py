#!/usr/bin/env python3

"""Maximum of all subarrays of size k."""


from itertools import islice


def maximum_of_all_subarrays(array, k: int):
    """Find all the maximum values of all subarrays of size k."""
    maximum_of_all = []
    for i in range(len(array)):
        subarray = list(islice(array, i, k+i))
        if len(subarray) == k:
            maximum_of_all.append(max(subarray))
        else:
            break

    return tuple(maximum_of_all)


if __name__ == "__main__":
    print(maximum_of_all_subarrays(array=(1, 2, 3, 1, 4, 5, 2, 3, 6,), k=3))
    print(maximum_of_all_subarrays(
        array=(8, 5, 10, 7, 9, 4, 15, 12, 90, 13,), k=4))

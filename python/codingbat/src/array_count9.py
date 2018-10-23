#!/usr/bin/env python3

"""Array Count 9.

Given an array of ints, return the number
of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

source: https://codingbat.com/prob/p166170
"""

from functools import partial


def array_count(nums: list, target: int) -> int:
    """Count of target in nums.

    :return: Integer number of target in nums list/array.
    """
    return len(list(filter(lambda x: x == target, nums)))


array_count9 = partial(array_count, target=9)


def main():
    """Array count 9 test methods."""
    assert array_count9([1, 2, 9]) == 1
    assert array_count9([1, 9, 9]) == 2
    assert array_count9([1, 9, 9, 3, 9]) == 3
    assert array_count9([1, 2, 3]) == 0
    assert array_count9([]) == 0
    assert array_count9([4, 2, 4, 3, 1]) == 0
    assert array_count9([9, 2, 4, 3, 1]) == 1
    print('Passed.')


if __name__ == "__main__":
    main()

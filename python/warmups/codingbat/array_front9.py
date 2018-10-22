#!/usr/bin/env python3

"""Array Front 9

Given an array of ints, return True if one of the
first 4 elements in the array is a 9.
The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

source: https://codingbat.com/prob/p110166

"""

from functools import partial


def array_front(nums: iter, target: int, length: int) -> bool:
    """Is the `target` in `nums` of a given `length`.

    :return: True if target in nums[:length]. False otherwise.
    """
    return target in nums[:length]


array_front9 = partial(array_front, target=9, length=4)


def main():
    assert array_front9([1, 2, 9, 3, 4]) is True
    assert array_front9([1, 2, 3, 4, 9]) is False
    assert array_front9([1, 2, 3, 4, 5]) is False
    assert array_front9([9, 2, 3]) is True
    assert array_front9([1, 9, 9]) is True
    assert array_front9([1, 2, 3]) is False
    assert array_front9([1, 9]) is True
    assert array_front9([5, 5]) is False
    assert array_front9([2]) is False
    assert array_front9([9]) is True
    assert array_front9([]) is False
    assert array_front9([3, 9, 2, 3, 3]) is True
    print('Passed.')


if __name__ == "__main__":
    main()

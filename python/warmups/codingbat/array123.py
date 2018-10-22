#!/usr/bin/env python3

"""Array 1 2 3.


Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True


source: https://codingbat.com/prob/p193604

"""

from functools import partial


def array_find(nums: list, target=None) -> bool:
    """Determine if target is in nums."""
    for i in range(len(nums)):
        if target == nums[i:i+3]:
            return True
    return False


array123 = partial(array_find, target=[1, 2, 3])


def main():
    """Test the array123 function."""
    assert array123([1, 1, 2, 3, 1]) is True
    assert array123([1, 1, 2, 4, 1]) is False
    assert array123([1, 1, 2, 1, 2, 3]) is True
    assert array123([1, 1, 2, 1, 2, 1]) is False
    assert array123([1, 2, 3, 1, 2, 3]) is True
    assert array123([1, 2, 3]) is True
    assert array123([1, 1, 1]) is False
    assert array123([1, 2]) is False
    assert array123([1]) is False
    assert array123([]) is False
    print('Passed.')


if __name__ == "__main__":
    main()

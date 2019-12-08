#!/usr/bin/env python3

"""Find the Largest Number in a List.

Create a function that takes a list of numbers.
Return the largest number in the list.

Source:
https://edabit.com/challenge/A7hyDnb72prWryeuY
"""


def find_largest_num(nums):
    """Find the largest number in the list."""
    return max(nums)


def main():
    """Run sample find_largest_num functions. Do not import."""
    assert find_largest_num([4, 5, 1, 3]) == 5
    assert find_largest_num([13, 27, 18, 26]) == 27
    assert find_largest_num([32, 35, 37, 39]) == 39
    assert find_largest_num([1000, 1001, 857, 1]) == 1001
    assert find_largest_num([27364, 837363, 736736, 73635]) == 837363
    assert find_largest_num([30, 2, 40, 3]) == 40
    assert find_largest_num([0, 1, 0, 0, 1]) == 1
    print('Passed.')


if __name__ == "__main__":
    main()

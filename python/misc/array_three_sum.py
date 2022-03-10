#!/usr/bin/env python3

"""Determine if the sum of three integers is equal to the given value.

Given an array of integers and a value, determine if there are any three
integers in the array whose sum equals the given value.

"""


def sum_three(array, target_sum):
    """Determine if three intergers equal to the target_sum."""
    _array = sorted(array)
    for index in range(len(_array)-2):
        left_pointer = index + 1
        right_pointer = len(_array) - 1
        while (left_pointer < right_pointer):
            _sum = sum([_array[index], _array[left_pointer],
                        _array[right_pointer]])
            if(_sum == target_sum):
                return True
            elif (_sum < target_sum):
                left_pointer += 1
            else:
                right_pointer -= 1

    return False


if __name__ == "__main__":
    print(sum_three(array=[7, 2, 9, 8, 1], target_sum=11))
    print(sum_three(array=[1, 4, 33, 6, 10, 8], target_sum=22))

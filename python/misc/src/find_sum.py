#!/usr/bin/env python3

"""Example find sum from a collection.

My take on the "How to: Work at Google — Example Coding/Engineering Interview"
YouTube link: https://www.youtube.com/watch?v=XKu_SEDAykw
"""


def find_sum_naive(collection, target):
    """Find the target sum of two numbers in collection.

    Naive method, iterate through string.
    :return: True if found, False otherwise.
    """
    for i in collection:
        for j in collection[1:]:
            if i + j == target:
                return True
    return False


def find_sum(collection, target):
    """Find the target sum of two numbers in collection.

    Pythonic method. Using list comprehensions.
    :return: True if found, False otherwise.
    """
    complements = [8-i for i in collection]
    return bool([value for value in collection if value in complements])


if __name__ == "__main__":
    list(map(print,
             (find_sum([1, 2, 3, 9], 8),
              find_sum([1, 2, 4, 4], 8), )
             )
         )

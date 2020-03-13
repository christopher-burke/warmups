#!/usr/bin/env python3

"""Check if a List Contains a Given Number.

Write a function to check if a list contains a particular number.

Source:
https://edabit.com/challenge/ZGezQDXsturZGpQcS
"""

from typing import List

def check(lst: list, search_element: int) -> bool:
    """Check if the list contains the search_element."""
    return any([True for i in lst if i == search_element])


def main():
    """Run sample check functions. Do not import."""
    assert check([1, 2, 3, 4, 5], 3) == True
    assert check([1, 1, 2, 1, 1], 3) == False
    assert check([1, 1, 2, 1, 5, 4, 7], 7) == True
    assert check([1, 1, 2, 1, 5, 4, 7], 8) == False
    assert check([5, 5, 5, 6], 5) == True
    assert check([], 5) == False
    print('Passed.')

if __name__ == "__main__":
    main()
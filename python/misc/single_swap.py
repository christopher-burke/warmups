#!/usr/bin/env python3

"""Single Letter Swaps.

Given an array of strings and an original string, write a function to
output an array of boolean values - True if the word can be formed from
the original word by swapping two letters only once and False otherwise.


Source:
https://edabit.com/challenge/xukQmQoGopXbQMdZj
"""

from typing import List


def validate_swaps(array: List, org_string: str) -> List:
    """Validate array items have single swapping two letters only once."""
    valid_swap = []
    for item in array:
        same_char = bool(set(org_string) == set(item))
        same_len = bool(len(org_string) == len(item))
        one_swap = len(set(
            ["".join(sorted(a))
             for a in zip(item, org_string)
             if a[0] != a[-1]
             ])) == 1
        valid_swap.append(same_char and same_len and one_swap)
    return valid_swap


def main():
    """Run sample validate_swaps functions. Do not import."""
    assert validate_swaps(['BACDE', 'EBCDA', 'BCDEA', 'ACBED'], 'ABCDE') == [
        True, True, False, False]
    assert validate_swaps(['32145', '12354', '15342', '12543'], '12345') == [
        True, True, True, True]
    assert validate_swaps(['9786', '9788', '97865', '7689'], '9768') == [
        True, False, False, False]
    assert validate_swaps(['123', '321', '132', '13', '12'], '213') == [
        True, False, False, False, False]
    assert validate_swaps(['123', '1234', '1235'], '12') == [
        False, False, False]
    assert validate_swaps(['123', '123', '123'], '133') == [
        False, False, False]
    assert validate_swaps(['132', '321', '213'], '123') == [True, True, True]
    print('Passed.')


if __name__ == "__main__":
    main()

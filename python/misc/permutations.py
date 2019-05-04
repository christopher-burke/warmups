#!/usr/bin/env python3

"""Permutations of a given string.

Given a string, print all permutations of a given string.

Source: https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
"""


from itertools import permutations


def itertools_permutations(text: str) -> list:
    """Return all permutations of text.

    Uses itertools.permutations.
    """
    return ["".join(_) for _ in list(permutations(text))]


def permutations_(text: list, start: int, end: int):
    """Print all permutations.

    Function adapted from source.

    source: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
    """
    if start == end:
        print(''.join(text))
    else:
        for i in range(start, end+1):
            text[start], text[i] = text[i], text[start]
            permutations_(text, start+1, end)
            text[start], text[i] = text[i], text[start]


if __name__ == "__main__":
    print(itertools_permutations('ABC'))
    permutations_(text=['A', 'B', 'C', ], start=0, end=2)

#!/usr/bin/env python3

"""Combinations.

Given a string, print all possible combinations, up to size k in
lexicographic sorted order.

For this example:
* 0 < k <= len(Input Text)
* All uppercase letters.

Source:
https://www.hackerrank.com/challenges/itertools-combinations/problem
"""

from itertools import combinations
from typing import List


def k_length_combinations(text: str, k: int) -> List:
    """Return a list of all possible combinations of text of up to length k."""
    combos = []
    if k > len(text):
        return []
    for i in range(1, k+1):
        combos.append([''.join(combo)
                       for combo in combinations(sorted(text), i)])
    return [item for sublist in list(combos) for item in sublist]


def map_print(iterables):
    """Map print function to print combinations on separate lines."""
    list(map(print, iterables))


def main():
    """Run sample k_length_combinations. Main method, do not import."""
    map_print(k_length_combinations('HACK', 2))
    map_print(k_length_combinations('PYTHON', 3))
    map_print(k_length_combinations('COMPUTER', 0))
    map_print(k_length_combinations('VSCODE', 6))


if __name__ == "__main__":
    main()

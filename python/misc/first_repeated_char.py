#!/usr/bin/env python3

"""Print the first repeated character in a string."""

from collections import defaultdict


def first_repeated_char_v1(input_str: str):
    """Return the first repeated character in string."""
    counter = defaultdict(int)
    for char in input_str:
        counter[char] += 1
        if counter[char] == 2:
            return char
    return None


def first_repeated_char_v2(input_str: str):
    counts = dict()
    for char in input_str:
        if char in counts:
            return char
        counts[char] = 1
    return None


if __name__ == "__main__":
    list(map(print,
             (first_repeated_char_v1("ABBA"),
              first_repeated_char_v1("ABCA"),
              first_repeated_char_v1("DBCABA"),
              first_repeated_char_v1("BCABA"),
              first_repeated_char_v1("ABC"),)
             )
         )
    list(map(print,
             (first_repeated_char_v2("ABBA"),
              first_repeated_char_v2("ABCA"),
              first_repeated_char_v2("DBCABA"),
              first_repeated_char_v2("BCABA"),
              first_repeated_char_v2("ABC"),)
             )
         )

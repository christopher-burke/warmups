#!/usr/bin/env python3

"""Capitalization Families.

Write a function that groups words by the number of capital letters.
Sort the object values by length in lexicographic order.

Source:
https://edabit.com/challenge/rbeuWab36FAiLj65m
"""


from string import ascii_uppercase
from collections import defaultdict, OrderedDict


def grouping(iterable) -> dict:
    """Group words by number capital letters."""
    capitalization_grouping = defaultdict(list)

    for word in iterable:
        number_of_capitals = len(
            [letter for letter in word if letter in ascii_uppercase])
        capitalization_grouping[number_of_capitals].append(word)

    for key in capitalization_grouping.keys():
        capitalization_grouping[key] = sorted(
            capitalization_grouping[key], key=lambda v: v.lower())
    return OrderedDict(sorted(capitalization_grouping.items()))


def main():
    """Run sample grouping function. Do not import."""
    assert grouping(["MOVIE", "TAKE", "PERSON"]) == {
        4: ["TAKE"],
        5: ["MOVIE"],
        6: ["PERSON"]}

    assert grouping(["the", "them", "theme", "EVERY"]) == {
        0: ["the", "them", "theme"],
        5: ["EVERY"]}

    assert grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]) == {
        0: ["yummy", ],
        2: ["mayBE",
            "mOOdy", ],
        3: ["HaPPy", ]}

    assert grouping(["eeny", "meeny", "miny", "moe"]) == {
        0: ["eeny", "meeny", "miny", "moe"]}

    assert grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]) == {
        0: ["lor", ],
        1: ["sOr", ],
        2: ["bOR", "MoR", "tOR", ],
        3: ["FORe", ]}
    print('Passed.')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""The Museum of Incredibly Dull Things.

A museum wants to get rid of some exhibitions.
Vanya, the interior architect, comes up with a plan to remove
the most boring exhibitions. She gives them a rating, and removes
the one with the lowest rating. Just as she finishes rating the
exhibitions, she's called off to an important meeting.
She asks you to write a program that tells her the ratings
of the items after the lowest one is removed.

Create a function that takes a list of integers and removes the smallest value.

Source:
https://edabit.com/challenge/cx7eFvQBzjauLgwgZ
"""


def remove_smallest(ratings: list) -> list:
    """Remove the smallest rating from list."""
    min_, index_ = ratings[0], 0
    for index, score in enumerate(ratings):
        if score < int(min_):
            min_ = score
            index_ = index
    ratings.pop(index_)
    return ratings


def main():
    """Run sample remove_smallest functions. Do not import."""
    print(remove_smallest([1, 2, 3, 4, 5]))
    print(remove_smallest([5, 3, 2, 1, 4]))
    print(remove_smallest([2, 2, 1, 2, 1]))


if __name__ == "__main__":
    main()

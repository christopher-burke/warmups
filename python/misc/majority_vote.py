#!/usr/bin/env python3

"""Majority Vote.

Create a function that returns the majority vote in a list.
A majority vote is an element that occurs > N/2 times in a list
(where N is the length of the list).

Source:
https://edabit.com/challenge/pQavNkBbdmvSMmx5x
"""

from collections import Counter


def majority_vote(iterable):
    """Find the majority voted item in iterable.

    Majority vote is an element that occurs > N/2 times.
    N = length of iterable.
    """
    cnt = Counter(iterable)
    length = len(iterable)
    majority = [item for item, count in cnt.items() if count > length/2]
    if majority:
        return majority[0]
    return None


def main():
    assert majority_vote(["A", "B", "B", "B", "A", "A"]) is None
    assert majority_vote(["B", "B", "B"]) == "B"
    assert majority_vote(["A", "B", "B"]) == "B"
    assert majority_vote(["A", "A", "B"]) == "A"
    assert majority_vote(["A", "A", "A", "B", "C", "A"]) == "A"
    assert majority_vote(["B", "A", "B", "B", "C", "A", "B", "B"]) == "B"
    assert majority_vote(["A", "B", "B", "A", "C", "C"]) is None
    assert majority_vote(["A", "B"]) is None
    assert majority_vote(["A"]) == "A"
    assert majority_vote([]) is None
    print("Passed.")


if __name__ == "__main__":
    main()

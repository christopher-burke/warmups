#!/usr/bin/env python3

"""Poker Full House.

Create a function that determines whether or not a player is holding a
Full House in their hand. A hand is represented as a list of 5 cards.
A full house is defined as a pair of cards and a three-of-a-kind.

To illustrate:
* ["A", "A", "A", "K", "K"] would be a Full House
* The player holds 3 aces and 2 kings.

Source:
https://edabit.com/challenge/uugzpwJXKdiESZbjM
"""

from collections import Counter


def is_full_house(hand) -> bool:
    """Determine if hand is a Full House."""
    check = all([1 if card_count in (2, 3,) else 0
                 for card_count in Counter(hand).values()])
    return check


def main():
    """Run sample is_full_house functions."""
    assert is_full_house(["A", "A", "A", "K", "K"]) is True
    assert is_full_house(["3", "J", "J", "3", "3"]) is True
    assert is_full_house(["10", "J", "10", "10", "10"]) is False
    assert is_full_house(["7", "J", "3", "4", "2"]) is False
    assert is_full_house(['10', 'J', '10', 'J', '10']) is True
    assert is_full_house(['10', 'J', 'J', '2', '2']) is False
    print('Passed.')


if __name__ == "__main__":
    main()

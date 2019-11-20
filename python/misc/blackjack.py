#!/usr/bin/env python3

"""Blackjack.

Create a function that takes a list of card numbers and checks
if the sum of their value exceeds 21. If the sum exceeds 21,
return True and if the sum is under or equal to 21,
return False. Values of the cards are as follows:

* 2-10 are their value.
* J-K (face cards) count as 10.
* Aces count either as 1 or 11 - play conservatively, so that if giving an ace a value of 11 causes you to lose and 1
allows you to win, then go with 1.

Source:
https://edabit.com/challenge/d4YpsSWkDvgefxBc4
"""


card_values = {"A": 11, "K": 10, "Q": 10, "J": 10}


def over_twenty_one(cards) -> bool:
    """Determine if sum is over 21."""
    total = None
    total = sum([card_values.get(x, x) for x in cards])
    if total <= 21:
        return False
    if ("A" in cards) and (total - 10 <= 21):
        return False
    return True


def main():
    """Run sample over_twenty_one functions. Do not import."""
    assert over_twenty_one(['A', 2, 3])is False
    assert over_twenty_one(['A', 'J', 'K'])is False
    assert over_twenty_one(['A', 'J', 'K', 'Q'])is True
    assert over_twenty_one([5, 3, 6, 6, 7, 9])is True
    print('Passed.')


if __name__ == "__main__":
    main()

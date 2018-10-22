#!/usr/bin/env python3

"""String Splosion.

Given a non-empty string like "Code"
return a string like "CCoCodCode".

    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'

source: https://codingbat.com/prob/p118366
"""

from itertools import accumulate
from functools import reduce
from operator import add


def string_splosion(str_: str) -> str:
    """
    Return a string accumulating the letters from the beginning.

    Example, 'Code' becomes 'CCoCodCode'.

    :return: String with accumulated letters.
    """
    return reduce(add, accumulate(str_))


def main():
    """Run tests for string_splosion."""
    assert string_splosion('Code') == 'CCoCodCode'
    assert string_splosion('abc') == 'aababc'
    assert string_splosion('ab') == 'aab'
    assert string_splosion('x') == 'x'
    assert string_splosion('fade') == 'ffafadfade'
    assert string_splosion('There') == 'TThTheTherThere'
    assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
    assert string_splosion('Bye') == 'BByBye'
    assert string_splosion('Good') == 'GGoGooGood'
    assert string_splosion('Bad') == 'BBaBad'
    print('Passed.')


if __name__ == "__main__":
    main()

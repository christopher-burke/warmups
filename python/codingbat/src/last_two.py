#!/usr/bin/env python3

"""Last Two.

Given a string, return the count of the number
of times that a substring length 2 appears in
the string and also as the last 2 chars of the
string, so "hixxxhi" yields 1
(we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

source: https://codingbat.com/prob/p145834
"""


def last_two(str_: str) -> int:
    """
    Return the count of the number of times that a substring length 2 appears.

    :return: count of substring appearances.
    """
    last_two_str = str_[-2:]
    matches = list(
        filter(
            lambda x: x == last_two_str,
            [
                str_[i:i+2] for i in range(len(str_[:-2]))
            ]
        )
    )
    return len(matches)


def main():
    """Run tests for last_two."""
    assert last_two('hixxhi') == 1
    assert last_two('xaxxaxaxx') == 1
    assert last_two('axxxaaxx') == 2
    assert last_two('xxaxxaxxaxx') == 3
    assert last_two('xaxaxaxx') == 0
    assert last_two('xxxx') == 2
    assert last_two('13121312') == 1
    assert last_two('11212') == 1
    assert last_two('13121311') == 0
    assert last_two('1717171') == 2
    assert last_two('hi') == 0
    assert last_two('h') == 0
    assert last_two('') == 0
    print('Passed.')


if __name__ == "__main__":
    main()

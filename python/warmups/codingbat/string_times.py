#!/usr/bin/env python3

"""String times.

Coding Bat Warmup.

string_times:

Given a string and a non-negative int n, return a larger string that is n
copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'

source: https://codingbat.com/prob/p193507
"""


def string_times(str_, n):
    """
    Take the string str_ times it by n and return it.

    :return: String times n
    """
    return str_ * n


def main():
    pass


if __name__ == "__main__":
    main()

    assert string_times('Hi', 2) == 'HiHi'
    assert string_times('Hi', 3) == 'HiHiHi'
    assert string_times('Hi', 1) == 'Hi'
    assert string_times('Hi', 0) == ''	''
    assert string_times('Hi', 5) == 'HiHiHiHiHi'
    assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
    assert string_times('x', 4) == 'xxxx'
    assert string_times('', 4) == ''	''
    assert string_times('code', 2) == 'codecode'
    assert string_times('code', 3) == 'codecodecode'

    print('Passed')

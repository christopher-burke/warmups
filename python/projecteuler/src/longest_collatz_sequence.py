#!/usr/bin/env python3

"""Longest Collatz sequence.


The following iterative sequence is defined
for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13,
we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE:   Once the chain starts the terms are
        allowed to go above one million.


source: https://projecteuler.net/problem=14
"""


from pprint import pprint
from collections import namedtuple
from itertools import accumulate


LongestCollatzSequence = namedtuple(
    'LongestCollatzSequence',
    'sequence length')


# def longest_collatz_sequence(limit: int = 1000000):
#
#    for i in range(2, limit+1):
#        CACHE[str(i)] = None
#        sequence = collatz_sequence(i)
#        CACHE[str(i)] = sequence
#
#    return max(CACHE.keys(), key=lambda k: len(CACHE[str(k)]))


CACHE = {'1': [1]}
CACHE_LENGTH = {'1': 1}


def longest_collatz_sequence(limit: int = 1000000):

    for i in range(2, limit+1):
        collatz_sequence_length(i)

    return max(CACHE_LENGTH.keys(), key=lambda k: CACHE_LENGTH[str(k)])


def collatz_sequence(n) -> int:
    """Get the sequence."""

    if CACHE.get(str(n)):
        return CACHE.get(str(n))

    next_ = int(n // 2) if n % 2 == 0 else int(3 * n + 1)

    sequence = [n] + collatz_sequence(next_)
    return sequence


def collatz_sequence_length(n) -> int:
    """Get the sequence length."""

    if CACHE_LENGTH.get(str(n)):
        return CACHE_LENGTH.get(str(n))

    next_ = int(n // 2) if n % 2 == 0 else int(3 * n + 1)

    CACHE_LENGTH[str(n)] = 1 + collatz_sequence_length(next_)

    return CACHE_LENGTH[str(n)]


def main():
    """Run Longest Collatz sequence."""
    return longest_collatz_sequence(1000000)


if __name__ == "__main__":

    lcs = main()

    print(lcs, collatz_sequence(int(lcs)))

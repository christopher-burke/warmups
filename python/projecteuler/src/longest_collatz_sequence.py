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


CACHE = {1: [1]}
CACHE_LENGTH = {1: 1}


def collatz_sequence(n) -> int:
    """Get the Collatz Sequence list.

    Add each found Collatz Sequence to CACHE.
    :return:
    """
    if n in CACHE:
        return CACHE[n]

    next_ = int(n // 2) if n % 2 == 0 else int(3 * n + 1)
    CACHE[n] = [n] + collatz_sequence(next_)

    return CACHE[n]


def longest_collatz_sequence(limit: int) -> int:
    """Find the longest Collatz Sequence length.

    :return: number that generates the longest collazt sequence.
    """
    for i in range(2, limit+1):
        collatz_sequence_length(i)
    longest = max(CACHE_LENGTH.keys(), key=lambda k: CACHE_LENGTH[k])

    return longest


def collatz_sequence_length(n):
    """Get the Collatz Sequence of n.

    :return: List of Collatz Sequence.
    """
    if n not in CACHE_LENGTH:
        next_ = int(n // 2) if n % 2 == 0 else int(3 * n + 1)
        CACHE_LENGTH[n] = 1 + collatz_sequence_length(next_)
    return CACHE_LENGTH[n]


def main() -> int:
    """Find the Longest Collatz sequence under 1,000,000.

    :return: Longest Collatz sequence under 1,000,000
    """
    return longest_collatz_sequence(1000000)


if __name__ == "__main__":
    lcs = main()
    print(lcs, CACHE_LENGTH[lcs])
    print(" → ".join(map(str, collatz_sequence(lcs))))

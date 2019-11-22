#!/usr/bin/env python3

"""Collatz Conjecture.

A Collatz sequence is generated like this. Start with a positive number. 
If it's even, halve it. If it's odd, multiply it by 3 and add one. 
Repeat the process with the resulting number. The Collatz Conjecture is
that every sequence eventually reaches 1 (continuing past 1 just results in
an endless repeat of the sequence (4, 2, 1)).

The length of the sequence from starting number to 1 varies widely.

Create a function that takes a number as an argument and returns a tuple of
two elements — the number of steps in the Collatz sequence of the number,
and the highest number reached.

Source:
https://edabit.com/challenge/Z8REdTE5P57f4q7dK
"""


def collatz_sequence(n: int):
    """Find the Collatz sequence of n."""
    CACHE = {1: [1]}
    if n in CACHE:
        return CACHE[n]
    next_ = int(n // 2) if n % 2 == 0 else int(3 * n + 1)
    CACHE[n] = [n] + collatz_sequence(next_)

    return CACHE[n]


def collatz(n: int):
    """Take number n and calculate steps and highest Collatz sequence."""
    sequence = collatz_sequence(n)
    return (len(sequence), max(sequence),)


def main():
    """Run sample functions. Do not import."""
    assert collatz(3) == (8, 16)
    assert collatz(7) == (17, 52)
    assert collatz(17) == (13, 52)
    assert collatz(42) == (9, 64)
    assert collatz(33) == (27, 100)
    print('Passed.')


if __name__ == "__main__":
    main()

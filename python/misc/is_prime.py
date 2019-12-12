#!/usr/bin/env python3

"""Is the number Prime.

Source:
https://edabit.com/challenge/G7KG4kaABpeYu2RBR
"""


def divisors(n: int):
    """Return list of divisors.

    Using list comprehension.
    n : int
    returns a list of divisor(s).
    """
    return [divisor for divisor in range(1, n+1) if n % divisor == 0]


def prime(n: int):
    """Determine if a number is prime.

    Prime numbers are divisible by 1 and itself.

    n: int
    returns True if prime and False if not prime.
    """
    return [1, n] == divisors(n)


is_prime = prime


def main():
    """Run sample is_prime functions."""
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(11) is True
    assert is_prime(102) is False
    assert is_prime(103) is True
    print('Passed.')


if __name__ == "__main__":
    main()

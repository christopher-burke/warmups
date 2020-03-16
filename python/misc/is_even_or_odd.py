#!/usr/bin/env python3

"""Is the Number Even or Odd.

Create a function that takes a number as an argument and returns "even"
for even numbers and "odd" for odd numbers.

Source:
https://edabit.com/challenge/DruRW8YM8PNiH9Kg7
"""


def is_even_or_odd(number: int) -> str:
    """Number `odd` or `even`."""
    return "even" if number % 2 == 0 else "odd"


def main():
    """Run sample is_even_or_odd functions. Do not import."""
    assert is_even_or_odd(3) == "odd"
    assert is_even_or_odd(0) == "even"
    assert is_even_or_odd(7) == "odd"
    assert is_even_or_odd(12) == "even"
    assert is_even_or_odd(6474) == "even"
    assert is_even_or_odd(3) == "odd"
    assert is_even_or_odd(301) == "odd"
    assert is_even_or_odd(-3) == "odd"
    assert is_even_or_odd(-0) == "even"
    assert is_even_or_odd(-7) == "odd"
    assert is_even_or_odd(-12) == "even"
    assert is_even_or_odd(-6474) == "even"
    assert is_even_or_odd(-3) == "odd"
    assert is_even_or_odd(-301) == "odd"
    print('Passed.')

if __name__ == "__main__":
    main()
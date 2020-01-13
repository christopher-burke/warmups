#!/usr/bin/env python3

"""Return the Next Number from the Integer Passed.

Create a function that takes a number as an argument,
increments the number by +1 and returns the result.

Source:
https://edabit.com/challenge/KjCS7occ9hfu5snpb
"""


def addition(num: int) -> int:
    """Increase num by one."""
    return num + 1


def main():
    """Run sample addition functions. Do not import."""
    assert addition(2) == 3
    assert addition(-9) == -8
    assert addition(0) == 1
    assert addition(999) == 1000
    assert addition(73) == 74
    print('Passed.')


if __name__ == "__main__":
    main()

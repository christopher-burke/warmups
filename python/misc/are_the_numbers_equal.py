#!/usr/bin/env python3

"""Are the Numbers Equal? - warmup.

Create a function that takes two integers and checks if they are equal.

Source:
https://edabit.com/challenge/Tbvjwh5GKRbxd3vyD
"""


def is_equal(a: int, b: int) -> bool:
    """Determine if a and b are equal numbers.

    Determine if both numbers are equal by subtracting.
    """
    if type(a) == int and type(b) == int:
        result = a - b
        return bool(result == 0)
    return False


def is_equal2(a: int, b: int) -> bool:
    """Determine if a and b are equal numbers.

    Determine if both numbers by comparing.
    """
    if type(a) == int and type(b) == int:
        return a == b
    return False


def main():
    """Run sample is_equal functions. Do not import."""
    assert is_equal(2, 2) == True
    assert is_equal("1", 5) == False
    assert is_equal(88, 88) == True
    assert is_equal(36, 35) == False
    assert is_equal("1", 1) == False
    assert is_equal(1, 1) == True
    assert is_equal(5, 6) == False
    print('is_equal Passed.')
    assert is_equal2(2, 2) == True
    assert is_equal2("1", 5) == False
    assert is_equal2(88, 88) == True
    assert is_equal2(36, 35) == False
    assert is_equal2("1", 1) == False
    assert is_equal2(1, 1) == True
    assert is_equal2(5, 6) == False
    print('is_equal2 Passed.')


if __name__ == "__main__":
    main()

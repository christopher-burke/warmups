#!/usr/bin/env python3

"""Divides Evenly.

Given two integers, a and b, return True if a can be divided evenly by b. 
Return False otherwise.

Source:
https://edabit.com/challenge/NRxWszQRw5JqSDmQS
"""


def divides_evenly(a: int, b: int) -> bool:
    """Determine if a can be divided by b evenly."""
    return bool(a % b == 0)


def main():
    """Run sample divides_evenly functions. Do not import."""
    assert divides_evenly(98, 7) is True
    assert divides_evenly(87, 49) is False
    assert divides_evenly(34, 14) is False
    assert divides_evenly(78, 6) is True
    assert divides_evenly(30, 4) is False
    assert divides_evenly(87, 73) is False
    assert divides_evenly(74, 7) is False
    assert divides_evenly(87, 29) is True
    assert divides_evenly(48, 24) is True
    assert divides_evenly(99, 20) is False
    assert divides_evenly(98, 49) is True
    assert divides_evenly(100, 6) is False
    assert divides_evenly(64, 4) is True
    assert divides_evenly(70, 35) is True
    assert divides_evenly(38, 38) is True
    assert divides_evenly(29, 3) is False
    print('Passed.')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""Less Than 100.

Given two numbers, return True if the sum of both numbers is less than 100.
Otherwise return False.

Source:
https://edabit.com/challenge/pZ3HxBfvejsvkEDo4
"""

def less_than_100(a:int, b: int) -> bool:
    """Determin if the sum of two numbers is less than 100."""
    return sum((a,b,)) < 100


def main():
    """Run sample less_than_100. Do not import."""
    assert less_than_100(5, 57) is True
    assert less_than_100(77, 30) is False
    assert less_than_100(0, 59) is True
    assert less_than_100(78, 35) is False
    assert less_than_100(63, 11) is True
    assert less_than_100(37, 99) is False
    assert less_than_100(52, 11) is True
    assert less_than_100(82, 95) is False
    assert less_than_100(17, 44) is True
    assert less_than_100(74, 53) is False
    assert less_than_100(3, 77) is True
    assert less_than_100(25, 80) is False
    assert less_than_100(59, 28) is True
    assert less_than_100(69, 87) is False
    assert less_than_100(10, 45) is True
    assert less_than_100(43, 58) is False
    assert less_than_100(50, 44) is True
    assert less_than_100(74, 89) is False
    assert less_than_100(3, 27) is True
    assert less_than_100(21, 79) is False
    print('Passed.')

if __name__ == "__main__":
    main()
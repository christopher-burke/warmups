#!/usr/bin/env python3

"""Happy Numbers.

Given any number, we can create a new number by adding the sums of squares of
digits of that number. Given a positive whole number, you have to determine
whether that number is happy or unhappy

Source:
https://edabit.com/challenge/knWLLoi87YbCmKJS4
"""


def happy(number: int) -> bool:
    """Determine if number is happy.

    True = happy
    False = unhappy
    """
    if number == 1:
        return True
    if number == 4:
        return False
    total = 0
    while total not in (1, 4,):
        while number > 0:
            digit = number % 10
            total = total + digit ** 2
            number = number // 10
        return happy(total)


def main():
    """Main function for running test happy functions. Do not import."""
    assert happy(100) is True
    assert happy(101) is False
    assert happy(102) is False
    assert happy(103) is True
    assert happy(104) is False
    assert happy(105) is False
    assert happy(106) is False
    assert happy(107) is False
    assert happy(108) is False
    assert happy(109) is True
    assert happy(110) is False
    print("Passed.")


if __name__ == "__main__":
    main()

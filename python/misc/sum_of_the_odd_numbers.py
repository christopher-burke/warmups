#!/usr/bin/env python3

"""Sum of the Odd Numbers.

Create a function which returns the total of all odd numbers up to and
including n. n will be given as an odd number.

Source:
https://edabit.com/challenge/CD5nkQ6ah9xayR3cJ
"""

from math import ceil


def add_odd_to_n(n: int) -> int:
    """Sum of all odd numbers to n inclusive."""
    return ceil(n/2) ** 2


def main():
    """Run sample add_odd_to_n functions. Do not import."""
    assert add_odd_to_n(1) == 1
    assert add_odd_to_n(3) == 4
    assert add_odd_to_n(5) == 9
    assert add_odd_to_n(7) == 16
    assert add_odd_to_n(9) == 25
    assert add_odd_to_n(11) == 36
    assert add_odd_to_n(13) == 49
    assert add_odd_to_n(15) == 64
    assert add_odd_to_n(17) == 81
    assert add_odd_to_n(19) == 100
    assert add_odd_to_n(21) == 121
    assert add_odd_to_n(23) == 144
    assert add_odd_to_n(25) == 169
    assert add_odd_to_n(27) == 196
    assert add_odd_to_n(29) == 225
    assert add_odd_to_n(31) == 256
    assert add_odd_to_n(33) == 289
    assert add_odd_to_n(35) == 324
    assert add_odd_to_n(37) == 361
    assert add_odd_to_n(39) == 400
    assert add_odd_to_n(41) == 441
    assert add_odd_to_n(43) == 484
    assert add_odd_to_n(45) == 529
    assert add_odd_to_n(47) == 576
    assert add_odd_to_n(49) == 625
    assert add_odd_to_n(51) == 676
    assert add_odd_to_n(53) == 729
    assert add_odd_to_n(55) == 784
    assert add_odd_to_n(57) == 841
    assert add_odd_to_n(59) == 900
    assert add_odd_to_n(61) == 961
    assert add_odd_to_n(63) == 1024
    assert add_odd_to_n(65) == 1089
    assert add_odd_to_n(67) == 1156
    assert add_odd_to_n(69) == 1225
    assert add_odd_to_n(71) == 1296
    assert add_odd_to_n(73) == 1369
    assert add_odd_to_n(75) == 1444
    assert add_odd_to_n(77) == 1521
    assert add_odd_to_n(79) == 1600
    assert add_odd_to_n(81) == 1681
    assert add_odd_to_n(83) == 1764
    assert add_odd_to_n(85) == 1849
    assert add_odd_to_n(87) == 1936
    assert add_odd_to_n(89) == 2025
    assert add_odd_to_n(91) == 2116
    assert add_odd_to_n(93) == 2209
    assert add_odd_to_n(95) == 2304
    assert add_odd_to_n(97) == 2401
    assert add_odd_to_n(99) == 2500
    print('Passed.')


if __name__ == "__main__":
    main()

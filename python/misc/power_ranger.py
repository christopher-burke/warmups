#!/usr/bin/env python3

"""Power Ranger.

Create a function that takes in n, a, b and returns the number of values
raised to the nth power lie in the range [a, b], inclusive.

Source:
https://edabit.com/challenge/abdsaD6gwjgAgevsG
"""


def power_ranger(power: int, minimum: int, maximum: int) -> int:
    """Count of values raised to power are in range [minimum, maximum]."""
    return len([base**power for base in range(1, maximum+1)
                if base**power >= minimum and base**power <= maximum])


def main():
    """Run sample power_ranger functions. Do not import."""
    assert power_ranger(5, 31, 33) == 1
    assert power_ranger(4, 250, 1300) == 3
    assert power_ranger(2, 49, 65) == 2
    assert power_ranger(3, 1, 27) == 3
    assert power_ranger(10, 1, 5) == 1
    assert power_ranger(1, 1, 5) == 5
    assert power_ranger(2, 1, 100) == 10
    print('Passed.')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""Seven Boom!

Create a function that takes a list of numbers and return "Boom!"
if the number 7 appears in the list. Otherwise, return
"there is no 7 in the list".

Source:
https://edabit.com/challenge/BokhFunYBvsvHEjfx
"""


def boom(iterable, target: int) -> str:
    """Find the target in iterable.

    Return 'Boom!' if found.
    Return f"there is no {target} in the list"
    """
    for number in iterable:
        if str(target) in str(number):
            return "Boom!"
    return f"there is no {target} in the list"


def seven_boom(iterable):
    """Boom! if 7 is found in iterable."""
    return boom(iterable=iterable, target=7)


def main():
    """Run sample seven_boom functions. Do not import."""
    assert seven_boom([2, 6, 7, 9, 3]) == 'Boom!'
    assert seven_boom([33, 68, 400, 5]) == 'there is no 7 in the list'
    assert seven_boom([86, 48, 100, 66]) == 'there is no 7 in the list'
    assert seven_boom([76, 55, 44, 32]) == 'Boom!'
    assert seven_boom([35, 4, 9, 37]) == 'Boom!'
    print("Passed.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""Find the Perimeter of a Rectangle.

Create a function that takes height and width and finds the perimeter of a rectangle.

Source:
https://edabit.com/challenge/Yx2a9B57vXRuPevGh
"""


def find_perimeter(height: int, width: int) -> int:
    """Find the perimeter of a rectangle."""
    return (height + width) * 2


def main():
    """Run sample find_perimeter functions. Do not import."""
    assert find_perimeter(6, 7) == 26
    assert find_perimeter(20, 10) == 60
    assert find_perimeter(2, 9) == 22
    print('Passed.')


if __name__ == "__main__":
    main()

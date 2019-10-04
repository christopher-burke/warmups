#!/usr/bin/env python3

"""Area of a Triangle.

Write a function that takes the base and height of a triangle and
return its area.

Source:
https://edabit.com/challenge/aWLTzrRsrw7RakYrN
"""


def tri_area(base: int, height: int) -> int:
    """Find the area of a triangle."""
    return (base * height) / 2


def main():
    """Run sample tri_area functions. Do not import."""
    assert tri_area(3, 2) == 3
    assert tri_area(5, 4) == 10
    assert tri_area(10, 10) == 50
    assert tri_area(0, 60) == 0
    assert tri_area(12, 11) == 66
    print('Passed.')


if __name__ == "__main__":
    main()

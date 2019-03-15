#!/usr/bin/env python3

"""Missing Third Angle.

You are given 2 out of 3 of the angles in a triangle, in degrees.

Write a function that classifies the missing angle as either "acute", "right", 
or "obtuse" based on its degrees.

Source:
https://edabit.com/challenge/PKPmS5zwefc7M5emK
"""


def calc_missing_angle(a: int, b: int) -> int:
    """Return the missing angle of a triangle in degrees."""
    return 180 - (a + b)


def angle_classifier(a: int) -> str:
    """Classify the angle.

    An acute angle is one smaller than 90 degrees.
    A right angle is one that is exactly 90 degrees.    
    An obtuse angle is one greater than 90 degrees
    (but smaller than 180 degrees).

    """
    if a > 90 and a < 180:
        return "obtuse"
    elif a < 90 and a > 0:
        return "acute"
    return "right"


def missing_angle(a: int, b: int) -> str:
    """Determine the class of the missing angle."""
    missing_angle = calc_missing_angle(a, b)
    result = angle_classifier(missing_angle)

    return result


def main():
    """Run missing angle."""
    print(missing_angle(27, 59))
    print(missing_angle(135, 11))
    print(missing_angle(45, 45))


if __name__ == "__main__":
    main()

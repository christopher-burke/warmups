#!/usr/bin/env python3

"""Volume of a Pizza.

Tom is a very methodic guy that loves geometry and pizza: he loves
them so much that, before eating a pizza, he calculates its radius
and its height. Now, he wants to know from you the total volume of
pizza that he swallowed!

You are given the two parameters that Tom measured:

* radius
* height

He tells you that if you multiply the height for the square of the
radius and multiply the result for the mathematical constant π (Pi),
you will obtain the total volume of the pizza. Implement a function
that returns the volume of the pizza as a whole number, rounding it 
to the nearest integer (and rounding up for numbers with .5 as
decimal part).

Source:
https://edabit.com/challenge/NyTjy8nmHj9bmxMTC
"""


from math import pi as π

def vol_pizza(radius:int, height:int) -> int:
    """Return the volume of pizza."""
    return round(radius**2 * height * π)

def main():
    """Run sample vol_pizza functions. Do not import."""
    assert vol_pizza(1, 1) == 3
    assert vol_pizza(7, 2) == 308
    assert vol_pizza(10, 2.5) == 785
    assert vol_pizza(15, 1.3) == 919
    assert vol_pizza(20, 1) == 1257
    assert vol_pizza(13, 2) == 1062
    print('Passed.')

if __name__ == "__main__":
    main()



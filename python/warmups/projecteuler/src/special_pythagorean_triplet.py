#!/usr/bin/env python3

"""Special Pythagorean triplet


A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which:

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.
Find the product abc.

source: https://projecteuler.net/problem=9
"""


def brute_force(goal=1000):
    """Brute force method to find Pythagorean triplet with some of goal.

    Since a < b < c:

    * a is less than a third (1/3) of the goal, (a < goal//3)
    * b is greater than a and less than half(1/2) of the goal (a < b < goal//2)
    * c is one of the remaining numbers (goal//2 <= c),
      c is goal minus the sum of a and b (goal - (a + b)).

    :param goal: The sum of the pythagorean triplet
    :return: Tuple of Pythagorean triplet whose sum is the goal
    or None if not found
    """
    a_numbers = range(goal//3, 2, -1)
    b_numbers = range(goal//2, 2, -1)

    pythagorean_triplet = [(a, b, c,)
                           for a in a_numbers
                           for b in b_numbers
                           for c in [(goal - (a + b)), ]
                           if a*a + b*b == c*c
                           ]

    return pythagorean_triplet[0] if pythagorean_triplet else None


def main():
    """Find Special Pythagorean triplet."""
    print(brute_force())


if __name__ == "__main__":
    main()

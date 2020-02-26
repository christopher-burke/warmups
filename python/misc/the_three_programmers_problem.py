#!/usr/bin/env python3

"""The Three Programmers Problem.

You hired three programmers and you (hopefully) pay them. Create a
function that takes three numbers (the hourly wage of each programmer)
and returns the difference between the highest-paid programmer and
the lowest-paid.

Source:
https://edabit.com/challenge/9zsDKijmBffmnk9AP
"""


def programmers(one, two, three):
    """Find the difference between the highest and lowest numbers."""
    pays = (one,two, three,)
    return max(pays) - min(pays)

def main():
    """Run sample programmers functions. Do not import."""
    assert programmers(1, 5, 9) == 8
    assert programmers(43, 33, 43) == 10
    assert programmers(88, 14, 23) == 74
    assert programmers(33, 72, 74) == 41
    assert programmers(147, 33, 526) == 493
    assert programmers(234, 345, 457) == 223
    print('Passed.')

if __name__ == "__main__":
    main()
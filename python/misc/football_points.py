#!/usr/bin/env python3

"""Football Points.

Create a function that takes the number of wins, draws and losses and
calculates the number of points a football team has obtained so far. 
A win receives 3 points, a draw 1 point and a loss 0 points.

Source:
https://edabit.com/challenge/gwqqc5p3oiFXRJAQm
"""

def football_points(win: int, draw: int, loss:int):
    """Calculate the number of points for a football team."""
    return (win * 3 + draw)


def main():
    """Run sample football_points functions. Do not import."""
    assert football_points(1, 2, 3) == 5
    assert football_points(5, 5, 5) == 20
    assert football_points(1, 0, 0) == 3
    assert football_points(0, 7, 0) == 7
    assert football_points(0, 0, 15) == 0
    print('Passed.')


if __name__ == "__main__":
    main()





#!/usr/bin/env python3

"""Frames per second.

Create a function that returns the number of frames shown in a
given number of minutes for a certain FPS.

Source:
https://edabit.com/challenge/Yj2Rew5XQYpu7Nosq
"""

def frames(minutes: int, fps: int) -> int:
    """Find the number of frames shown."""
    seconds = minutes * 60
    return seconds * fps

def main():
    """Run sample functions. Do not import."""
    assert frames(1, 1) == 60
    assert frames(10, 1) == 600
    assert frames(10, 25) == 15000
    assert frames(500, 60) == 1800000
    assert frames(0, 60) == 0
    assert frames(99, 1) == 5940
    assert frames(419, 70) == 1759800
    assert frames(52, 33) == 102960
    print('Passed.')
    

if __name__ == "__main__":
    main()
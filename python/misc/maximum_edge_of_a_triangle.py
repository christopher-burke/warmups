#!/usr/bin/env python3

"""Maximum Edge of a Triangle.

Create a function that finds the maximum range of a triangles third edge.

Source:
https://edabit.com/challenge/Zerwo2AENbvRZTe83
"""


def next_edge(side_1: int, side_2: int) -> int:
    """Find the maximum range of a triangles third edge."""
    return (side_1 + side_2) - 1


def main():
    """Run sample next_edge. Do not import."""
    assert next_edge(5, 4) == 8
    assert next_edge(8, 3) == 10
    assert next_edge(7, 9) == 15
    assert next_edge(10, 4) == 13
    assert next_edge(7, 2) == 8
    print('Passed.')


if __name__ == "__main__":
    main()

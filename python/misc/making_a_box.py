#!/usr/bin/env python3

"""Making a Box.

Create a function that creates a box based on dimension n.

Source:
https://edabit.com/challenge/dy3WWJr34gSGRPLee
"""


def make_box(n: int, character: str = '#') -> list:
    """Create a box on dimension n using character."""
    box = []
    for i in range(n):
        if i in (0, n-1):
            box.append(f'{character*n}')
        else:
            box.append(f'{character}{" "*(n-2)}{character}')
    return box


def main():
    """Run sample make_box functions. Do not import."""
    assert make_box(5) == [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ]
    assert make_box(6) == [
        "######",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        "######"]

    assert make_box(4) == [
        "####",
        "#  #",
        "#  #",
        "####"]

    assert make_box(2) == [
        "##",
        "##"]

    assert make_box(1) == [
        "#"
    ]
    print('Passed.')


if __name__ == "__main__":
    main()

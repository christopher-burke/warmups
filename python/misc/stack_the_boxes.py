#!/usr/bin/env python3

"""Stack the Boxes.

Write a function that takes a number n and returns the number of stacked boxes
in a model n levels high, visible and invisible.

Source:
https://edabit.com/challenge/SKdpWwgKMAwMPHvRK
"""


def stack_boxes(boxes: int):
    """Number of boxes that can be stacked."""
    return boxes * boxes


def main():
    """Run sample functions. Do not import."""
    assert stack_boxes(1) == 1
    assert stack_boxes(2) == 4
    assert stack_boxes(0) == 0
    assert stack_boxes(5) == 25
    assert stack_boxes(27) == 729
    assert stack_boxes(196) == 38416
    assert stack_boxes(512) == 262144
    print('Passed.')

if __name__ == "__main__":
    main()
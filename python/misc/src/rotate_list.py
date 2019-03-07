#!/usr/bin/env python3

"""Rotate a Linked List.

Given a singly linked list of size N.
The task is to rotate the linked list counter-clockwise by k nodes,
where k is a given positive integer smaller than or equal to length
of the linked list.

Source:
https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1
"""


def rotate(items: list, k: int) -> list:
    """Rotate a list by k elements."""
    items = items[k:] + items[:k]
    return items


def main():
    """Rotate list samples."""
    print(rotate(items=[1, 2, 3, 4, 5, 6, 7, 8, ], k=4))
    print(rotate(items=[0, 1, 2, 3], k=0))
    print(rotate(items=[22, 8, 1, 27], k=3))


if __name__ == "__main__":
    main()

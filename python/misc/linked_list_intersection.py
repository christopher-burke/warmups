#!/usr/bin/env python3

"""Intersection Point of Two Linked Lists.


Given the head nodes of two linked lists that may or may not intersect, 
find out if they do in fact intersect and return the point of intersection. 
Return null otherwise.

In the below example, neither lists intersects. Intersect() should return NULL.

For this example we'll use None instead of NULL. And return the starting 
position on both linked lists.
"""


from typing import List, NoReturn


def _helper(length_diff, linked_list):
    """Helper function for longer linked list."""
    length_diff = abs(length_diff)
    return linked_list[length_diff:]


def intersect(linked_list_1: List, linked_list_2: List):
    """Intersection point of two linked list."""
    length_diff = len(linked_list_1) - len(linked_list_2)
    enum1 = list(enumerate(linked_list_1))
    enum2 = list(enumerate(linked_list_2))

    if length_diff < 0:
        enum2 = _helper(length_diff=length_diff, linked_list=enum2)
    else:
        enum1 = _helper(length_diff=length_diff, linked_list=enum1)

    for (i, j,) in zip(enum1, enum2):
        if i[1] == j[1]:
            return (i[0], j[0],)
    return None


def main() -> NoReturn:
    """Run intersect."""
    result = intersect(
        linked_list_1=[13, 4, 12, 27, ],
        linked_list_2=[29, 23, 82, 11, 12, 27, ]
    )
    print(result)


if __name__ == "__main__":
    main()

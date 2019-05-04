#!/usr/bin/env python3

"""Finding middle element in a linked list.

Given a singly linked list of N nodes. The task is to find middle of the linked list. 
For example, if given linked list is 
1->2->3->4->5 then output should be 3. 

If there are even nodes, then there would be two middle nodes,
we need to print second middle element. 
For example, if given linked list is
1->2->3->4->5->6 then output should be 4.

Source:
https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
"""


def middle(items: list):
    """Return middle item in list."""
    length = len(items) // 2

    return items[length]


def main():
    """Run sample middle functions."""
    print(middle([1, 2, 3, 4, 5, ]))
    print(middle([2, 4, 6, 7, 5, 1, ]))
    print(middle([222, 12, 10, 45, 5, ]))
    print(middle([1, 2, 3, 4, 5, 6, ]))


if __name__ == "__main__":
    main()

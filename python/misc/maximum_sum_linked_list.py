#!/usr/bin/env python3


"""Maximum sum of linked list.

Code challenge:

Given a linked list of integers. Determine the maximum sum
only considering the first and last item of the linked list.

Example:
A list containting [4, 2, 3, 5]. Would produce:

* 4,5 = 9
* 2,3 = 5

The result would be 9.

"""

from typing import List


class Node:
    """Node class containing data and next Node."""
    next = None
    data = None


class LinkedList:
    """Single Linked List of Nodes."""

    def __init__(self, ints: List[int] = None) -> None:
        if ints:
            self.create_nodes(node_values=node_values)
            self.head = self.create_linked_list()
        else:
            raise ValueError(f"List needed. Value provided: {ints=}.")

    def create_node(self, data=None) -> Node:
        """Create a node with data."""
        node = Node()
        node.data = data
        return node

    def create_nodes(self, node_values: List) -> None:
        """Create linked list with node values."""
        self.nodes = tuple(self.create_node(data=value)
                           for value in node_values)

    def create_linked_list(self, nodes=None):
        """Create a linked list."""
        if nodes is None:
            nodes = self.nodes
        nodes = self.nodes
        self.head = None
        pointer = None
        for i, v in enumerate(nodes):
            if i == 0:
                head = v
                pointer = head
            if i + 1 <= len(nodes):
                try:
                    pointer.next = nodes[i + 1]
                    pointer = pointer.next
                except IndexError:
                    break
        return head


def remove_first(head_node: Node) -> Node:
    """Remove first item in linked list."""
    current = head_node
    return current


def remove_last(head_node: Node) -> Node:
    """Remove the last item in linked list."""
    previous = None
    current = head_node
    while current.next:
        previous = current
        current = current.next
    try:
        previous.next = None
    except AttributeError:
        return None
    return current


def get_value(node: Node) -> int:
    """Return node value."""
    return node.data if node else 0


def maximum_sum(head_node) -> int:
    """Maximum sum of the first and last nodes of a link list."""
    d = []
    if not head_node.next:
        print("No next")
    while head_node:
        d.append([get_value(remove_first(head_node=head_node)),
                  get_value(remove_last(head_node=head_node)), ])
        head_node = head_node.next
    return max([sum(i) for i in d])


if __name__ == "__main__":
    samples = [
        (None, None),
        (7, [4, 2, 1, 2, 3, ],),
        (10, [4, 2, 6, 4, 2, 3, ],),
        (100, [1, 2, 3, 40, 5, 6, 7, 99, ]),
        (200, list(reversed(list(range(101)))) + list(range(101))),
    ]

    for expected, node_values in samples:
        try:
            head = LinkedList(ints=node_values)
            print(maximum_sum(head_node=head.head))
        except ValueError:
            print(f"Invalid input: {node_values=}.")

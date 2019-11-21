#!/usr/bin/env python3

"""Remove Duplicates from a List.

Create a function that takes a list of items, removes all duplicate
items and returns a new list in the same sequential order as the old
list (minus duplicates).

Source:
https://edabit.com/challenge/SLCqbNTy4aacoNjvw
"""


from collections import OrderedDict


def remove_dups(lst):
    """Remove duplicates from a List."""
    set_ = OrderedDict()

    for item in lst:
        set_[item] = None

    return list(set_.keys())


def main():
    assert remove_dups(['John', 'Taylor', 'John']) == ['John', 'Taylor']
    assert remove_dups(['John', 'Taylor', 'John', 'john']) == [
        'John', 'Taylor', 'john']
    assert remove_dups(['javascript', 'python', 'python', 'ruby', 'javascript', 'c', 'ruby']) == [
        'javascript', 'python', 'ruby', 'c']
    assert remove_dups([1, 2, 2, 2, 3, 2, 5, 2, 6, 6, 3, 7, 1, 2, 5]) == [
        1, 2, 3, 5, 6, 7]
    assert remove_dups(['#', '#', '%', '&', '#', '$', '&']) == [
        '#', '%', '&', '$']
    assert remove_dups([3, 'Apple', 3, 'Orange', 'Apple']) == [
        3, 'Apple', 'Orange']
    print('Passed.')


if __name__ == "__main__":
    main()

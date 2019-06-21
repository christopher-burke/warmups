#!/usr/bin/env python3

"""Concatenate Variable Number of Input Lists.

Create a function that concatenates n input lists, where n is variable.

Lists should be concatenated in order of the arguments.

Source:
https://edabit.com/challenge/woA74HtrheoQva87R
"""


def concat(*args) -> list:
    """Concatenates n input lists(*args), where n is variable."""
    # Create an empty list to return
    return_list = []

    # Add each list item in *args to the return_list.
    # += adds each item in i one by one.
    for i in args:
        return_list += i

    return return_list


def main():
    """Run sample concat functions with assert statements. Do not import."""
    # Assert statements for 'concat'.
    assert concat([1, 2, 3], [4, 5], [6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert concat([1], [2], [3], [4], [5], [6], [7]) == [1, 2, 3, 4, 5, 6, 7]
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert concat([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]
    assert concat(['a'], ['b', 'c']) == ['a', 'b', 'c']
    print("Function 'concat' completed successful.")


if __name__ == "__main__":
    main()

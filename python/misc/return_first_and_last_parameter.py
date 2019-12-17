#!/usr/bin/env python3

"""Return First and Last Parameter.

Write two functions:

* first_arg() should return the first parameter passed in.
* last_arg() should return the last parameter passed in.

Return None if the function takes no parameters.
"""


from functools import partial


def get_arg(*args, index: int):
    """Get the argument at index."""
    if args:
        return args[index]
    return None


first_arg = partial(get_arg, index=0)
last_arg = partial(get_arg, index=-1)


def main():
    """Run sample first_arg and last_arg functions."""
    assert first_arg(1, 2, 3) == 1
    assert first_arg('a', 'b', 'c') == 'a'
    assert first_arg(8) == 8
    assert first_arg() is None
    assert last_arg(1, 2, 3) == 3
    assert last_arg('a', 'b', 'c') == 'c'
    assert last_arg(8) == 8
    assert last_arg() is None
    print('Passed.')


if __name__ == "__main__":
    main()

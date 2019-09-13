#!/usr/bin/env python3

"""Match the Last Item.

Create a function that takes a list of items and checks if the last item
matches the rest of the list.

Source:
https://edabit.com/challenge/oGkwLhmpys95rjtQ2
"""


def match_last_item(items: list) -> bool:
    """Check if last item matches the rest of the list."""
    first_items, last_item = items[:-1], items[-1]
    first_items = [str(item) for item in first_items]
    return "".join(first_items) == last_item


def main():
    """Run sample match last items. Do not import."""
    assert match_last_item(['rsq', '6hi', 'g', 'rsq6hig']) is True
    assert match_last_item([0, 1, 2, 3, 4, 5, '12345']) is False
    assert match_last_item(['for', 'mi', 'da', 'bel', 'formidable']) is False
    assert match_last_item([8, 'thunder', True, '8thunderTrue']) is True
    assert match_last_item([1, 1, 1, '11']) is False
    assert match_last_item([
        'tocto', 'G8G', 'xtohkgc',
        '3V8', 'ctyghrs', 100.88,
        'fyuo', 'Q',
        'toctoG8Gxtohkgc3V8ctyghrs100.88fyuoQ']) is True
    print('Passed.')


if __name__ == "__main__":
    main()

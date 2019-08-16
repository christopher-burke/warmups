#!/usr/bin/env python3

"""Return the Objects Keys and Values.

Create a function that takes a dictionary and returns
the keys and values as separate lists.

Source:
https://edabit.com/challenge/9HWMgvjF7p3zhWBdk
"""


def keys_and_values(d):
    """Return the keys and values as separate lists.

    Sorted by the key value.
    """
    return [list(keys_values)
            for keys_values
            in list(zip(*sorted(list(d.items()))))]


def main():
    """Run sample functions. Do not import."""
    assert keys_and_values({'a': 1, 'b': 2, 'c': 3}) == [
        ["a", "b", "c"], [1, 2, 3]]
    assert keys_and_values({'a': "Apple", 'b': "Microsoft", 'c': "Google"}) == [
        ["a", "b", "c"], ["Apple", "Microsoft", "Google"]]
    assert keys_and_values({'key1': True, 'key2': False, 'key3': True}) == [
        ["key1", "key2", "key3"], [True, False, True]]
    assert keys_and_values({'key1': "cat", 'key2': "dog", 'key3': "fox"}) == [
        ["key1", "key2", "key3"], ["cat", "dog", "fox"]]
    print('Passed.')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""Sort a String by its Last Character.

Create a function that takes a string of words and return a string sorted
alphabetically by the last character of each word.

Source:
https://edabit.com/challenge/ic9aKYukaRH2MjDyk
"""


def sort_by_last(txt):
    """Sort string txt by each word's last character."""
    return " ".join(sorted(
        [word for word in txt.split(' ')],
        key=lambda x: x[-1].lower()
    ))


def assert_equals(func_result, result):
    """Assert equal the func_result with the desired result."""
    assert func_result == result, f"'{func_result}' does not match '{result}'."


def main():
    """Run sample sort_by_last functions. Do not import."""
    assert_equals(sort_by_last("herb camera dynamic"), "camera herb dynamic")
    assert_equals(sort_by_last("stab traction artist approach"),
                  "stab approach traction artist")
    assert_equals(sort_by_last("sample partner autonomy swallow trend"),
                  "trend sample partner swallow autonomy")
    assert_equals(sort_by_last("dividend platform pupil conclusion silence breakfast"),
                  "dividend silence pupil platform conclusion breakfast")
    assert_equals(sort_by_last("harm"), "harm")
    assert_equals(sort_by_last("card warrant opinion medium illustrate"),
                  "card illustrate medium opinion warrant")
    assert_equals(sort_by_last("cause fine virtue"), "cause fine virtue")
    assert_equals(sort_by_last("introduce fashionable cause sacrifice reality"),
                  "introduce fashionable cause sacrifice reality")
    assert_equals(sort_by_last("brick moral institution loud talk resign worth"),
                  "loud worth brick talk moral institution resign")
    print('Passed.')


if __name__ == "__main__":
    main()

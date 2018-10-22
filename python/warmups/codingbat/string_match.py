#!/usr/bin/env python3

"""String Match.

Given 2 strings, a and b, return the number of the positions
where they contain the same length 2 substring.

So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa",
and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

source: https://codingbat.com/prob/p182414
"""

from functools import partial


def string_match_(a, b, length):
    """Number of postions where they contain the same length substring."""
    zipped_substrings = list(
        zip(
            [a[i:i+length]
                for i in range(len(a))
                if len(a[i:i+length]) == length],
            [b[i:i+length]
                for i in range(len(b))
                if len(a[i:i+length]) == length]
        )
    )

    matches = list(filter(lambda x: x[0] == x[1], zipped_substrings))
    return len(matches)


string_match = partial(string_match_, length=2)


def main():
    """Test the string_match function."""
    assert string_match('xxcaazz', 'xxbaaz') == 3
    assert string_match('abc', 'abc') == 2
    assert string_match('abc', 'axc') == 0
    assert string_match('hello', 'he') == 1
    assert string_match('he', 'hello') == 1
    assert string_match('h', 'hello') == 0
    assert string_match('', 'hello') == 0
    assert string_match('aabbccdd', 'abbbxxd') == 1
    assert string_match('aaxxaaxx', 'iaxxai') == 3
    assert string_match('iaxxai', 'aaxxaaxx') == 3
    print('Passed.')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""Hello Name.

Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

source: https://codingbat.com/prob/p115413
"""


def hello_name(name: str) -> str:
    """Return `Hello name!`.

    :return:`Hello name!`
    """
    return f'Hello {name}!'


def main():
    """Main tests for hello_name."""
    assert hello_name('Bob') == 'Hello Bob!'
    assert hello_name('Alice') == 'Hello Alice!'
    assert hello_name('X') == 'Hello X!'
    assert hello_name('Dolly') == 'Hello Dolly!'
    assert hello_name('Alpha') == 'Hello Alpha!'
    assert hello_name('Omega') == 'Hello Omega!'
    assert hello_name('Goodbye') == 'Hello Goodbye!'
    assert hello_name('ho ho ho') == 'Hello ho ho ho!'
    assert hello_name('xyz!') == 'Hello xyz!!'
    assert hello_name('Hello') == 'Hello Hello!'
    print('Passed.')


if __name__ == "__main__":
    main()

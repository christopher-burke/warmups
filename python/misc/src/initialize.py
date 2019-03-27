#!/usr/bin/env python3

"""Initialize.

Turn full names into initials.

Source:
https://edabit.com/challenge/ANsubgd5zPGxov3u8
"""


def __initialize(name: str, period: bool=False) -> str:
    """Turn full name string into a initials string.

    Private function used by initialize.

    Arguments:
        name {[str]} -- Full name to be initialized.

    Keyword Arguments:
        period {bool} -- Include periods in initials (default: {False})

    Returns:
        [str] -- Initials string.

    """
    if period:
        return f"{'.'.join([n[0] for n in name.split(' ')])}."
    return ''.join([n[0] for n in name.split(' ')])


def initialize(names: list, **kwargs) ->list:
    """Turn a list of full names into a list of initials.

    Arguments:
        names {list} -- List of full names, with a space between each name.

    Raises:
        TypeError -- Check for names is a list.

    Returns:
        list -- All names initialized.

    """
    if isinstance(names, list):
        return [__initialize(name.strip(), **kwargs) for name in names if len(name) > 2 and ' ' in name]
    else:
        raise TypeError('Parameter \'names\' is not a list.')


def main():
    """Run sample initialize function."""
    print(initialize(['Peter Parker', 'Steve Rogers', 'Tony Stark']))
    print(initialize(
        ['Bruce Wayne', 'Clark Kent', 'Diana Prince'], period=True))


if __name__ == "__main__":
    main()

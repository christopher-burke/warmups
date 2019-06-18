#!/usr/bin/env python3

"""Current Military Time."""


from datetime import datetime as dt


def current_military_time():
    """Return the current military time."""
    return dt.now().strftime('%H:%M')


def main():
    """Run current_military_time function. Do not import."""
    print(current_military_time())


if __name__ == "__main__":
    main()

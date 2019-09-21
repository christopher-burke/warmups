#!/usr/bin/env python3

"""Fiscal Year.

Determine the fiscal year based on July 1 to June 30.
"""

from datetime import datetime, date


def fiscal_year(now=None):
    """Determine the fiscal year based on today's date."""
    if not now:
        now = datetime.now()
    if now.month >= 1 and now.month < 7:
        return now.year - 1
    return now.year


def main():
    """Run sample fiscal_year functions. Do not import."""
    assert fiscal_year(date(2018, 6, 6)) == 2017
    assert fiscal_year(date(2019, 7, 6)) == 2019
    assert fiscal_year(date(2001, 7, 6)) == 2001
    assert fiscal_year(date(2010, 6, 6)) == 2009
    print('Passed.')


if __name__ == "__main__":
    main()

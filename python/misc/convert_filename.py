#!/usr/bin/env python3

"""Convert file names.

For each file name convert to lowercase, replace spaces with underscores and add
date as a prefix.
"""


from datetime import datetime as dt


def date_prefix_helper() -> str:
    """Helper functions to get date prefix."""
    date_prefix = '{0:%Y_%m_%d}'.format(dt.now())
    return date_prefix



def update_filename(filename: str) -> str:
    """Convert filename.
    
    Convert filename to lowercase, replace spaces with underscores and add
    date prefix.
    """
    date_prefix = date_prefix_helper()
    filename_ = filename.lower()
    filename_ = filename_.replace(' ', '_')
    return f'{date_prefix}_{filename_}'


def main():
    """Run sample update_filename functions. Do not import."""
    assert update_filename('Test file') == f'{date_prefix_helper()}_test_file'
    assert update_filename('awesomeFILEname')  == f'{date_prefix_helper()}_awesomefilename'
    assert update_filename('insert TEXT here!.py')  == f'{date_prefix_helper()}_insert_text_here!.py'
    print('Passed.')


if __name__ == "__main__":
    main()
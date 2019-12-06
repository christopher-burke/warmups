#!/usr/bin/env python3

"""ASCII Charts (Part 1: Progress Bar).

Given a character and a value between 0 and 100, return a string that
represents a simple progress bar.

* The value represents a percentage.
* The bar should begin and end with "|"
* Repeat the character to fill the bar, with each character equivalent to 10%
* Use spaces to pad the bar to a length of 10 characters.
* A single space comes after the bar, then a message with the %
completion (e.g. "Progress: 60%")
* If the value is 100, the message should be "Completed!".


Source:
https://edabit.com/challenge/hwTRPKBat82XmcJWk
"""


def progress_bar(bar, progress):
    """Create an ASCII progress bar."""
    if progress == 100:
        return f"|{bar * 10}| Completed!"
    bar_count = progress // 10
    spaces = 10 - bar_count
    return f"|{bar * bar_count}{' ' * spaces}| Progress: {progress}%"


def progress_bar(bar, progress):
    """Create an ASCII progress bar."""
    if progress == 100:
        return f"|{bar * 10}| Completed!"  # using f-strings
    bar_count = progress // 10
    spaces = 10 - bar_count
    # using f-strings
    return f"|{bar * bar_count}{' ' * spaces}| Progress: {progress}%"


def main():
    """Run sample progress_bar functions. Do not import."""
    assert progress_bar("=", 10) == "|=         | Progress: 10%"
    assert progress_bar("#", 90) == "|######### | Progress: 90%"
    assert progress_bar("*", 100) == "|**********| Completed!"
    assert progress_bar("#", 50) == "|#####     | Progress: 50%"
    assert progress_bar("*", 60) == "|******    | Progress: 60%"
    assert progress_bar("#", 100) == "|##########| Completed!"
    assert progress_bar("*", 60) == "|******    | Progress: 60%"
    assert progress_bar("=", 30) == "|===       | Progress: 30%"
    assert progress_bar(">", 70) == "|>>>>>>>   | Progress: 70%"
    assert progress_bar("=", 40) == "|====      | Progress: 40%"
    assert progress_bar(">", 20) == "|>>        | Progress: 20%"
    assert progress_bar("*", 0) == "|          | Progress: 0%"
    assert progress_bar("=", 60) == "|======    | Progress: 60%"
    assert progress_bar(">", 90) == "|>>>>>>>>> | Progress: 90%"
    assert progress_bar("*", 80) == "|********  | Progress: 80%"
    assert progress_bar("#", 20) == "|##        | Progress: 20%"
    assert progress_bar("*", 30) == "|***       | Progress: 30%"
    assert progress_bar("=", 70) == "|=======   | Progress: 70%"
    assert progress_bar("=", 0) == "|          | Progress: 0%"
    assert progress_bar(">", 100) == "|>>>>>>>>>>| Completed!"
    print('Passed.')


if __name__ == "__main__":
    main()

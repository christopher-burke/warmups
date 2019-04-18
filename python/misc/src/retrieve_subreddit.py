#!/usr/bin/env python3

"""Retrieve the Subreddit.

Create a function to extract the name of the subreddit from its URL.

Source:
https://edabit.com/challenge/KoEqRNp5q27xsy9KE
"""

import re


def sub_reddit(url: str) -> str:
    """Extract the name of the subreddit from url.

    :param url: string url
    :returns : subreddit name
    """
    return re.match(r"https://www.reddit.com/r/(\w+)/", url).group(1)


def main():
    """Run sample sub_reddit functions. Do not import."""
    print(sub_reddit("https://www.reddit.com/r/funny/"))
    print(sub_reddit("https://www.reddit.com/r/relationships/"))
    print(sub_reddit("https://www.reddit.com/r/mildlyinteresting/"))


if __name__ == "__main__":
    main()

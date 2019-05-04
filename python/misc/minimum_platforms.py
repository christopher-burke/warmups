#!/usr/bin/env python3

"""Minimum Platforms.

Given arrival and departure times of all trains that reach a railway station.
Your task is to find the minimum number of platforms required for the railway
station so that no train waits.

Note: Consider that all the trains arrive on the same day and leave on the same day.
Also, arrival and departure times must not be same for a train.

source: https://practice.geeksforgeeks.org/problems/minimum-platforms/0
"""


def minimum_platforms(arrivals, departures) -> int:
    """Determine the number of platforms needed.

    Based on a collection of arrival and departure times.
    """
    # Total Minimum Platforms needed.
    minimum_platforms_needed = 0
    # Current number of platforms needed.
    platforms_needed = 0

    # Sort the arrival and departure times.
    times = [int(a) for a in arrivals] + [int(d) for d in departures]
    times = [str(time) for time in sorted(times)]

    # Iterate over the times and determine the minimum platforms needed.
    for time in times:
        if time in arrivals:
            platforms_needed += 1
        if time in departures:
            platforms_needed -= 1
        if platforms_needed > minimum_platforms_needed:
            minimum_platforms_needed = platforms_needed

    return minimum_platforms_needed


if __name__ == "__main__":
    arrival_times = '900  940 950  1100 1500 1800'.split()
    departure_times = '910 1200 1120 1130 1900 2000'.split()
    print(minimum_platforms(arrival_times, departure_times))

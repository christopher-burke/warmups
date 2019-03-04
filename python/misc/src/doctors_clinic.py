#!/usr/bin/env python3

"""Doctors Clinic.

Given two positive integers N and X, where N is the number of total patients
and X is the time duration(in minutes) after which a new patient arrives.

Also, doctor will give only 10 minutes to each patient.
The task is to calculate the time (in minutes) the last patient needs to wait.

Source: https://practice.geeksforgeeks.org/problems/doctors-clinic/0
"""


def last_patient_wait_time(total_patients: int, time_duration: int) -> int:
    """Calculate the wait time for the last patient.

    Return wait time in minutes.
    """
    # Find the max wait time for all patients ahead of the last patient.
    total_max_wait = ((total_patients - 1) * time_duration)
    # Find the total patient time of all patients ahead of the last patient.
    total_patient_time = (10 * (total_patients - 1))
    # Return the difference.
    last_patient_wait_time = total_patient_time - total_max_wait

    return last_patient_wait_time


def main():
    """Print samples."""
    print(last_patient_wait_time(total_patients=4, time_duration=5))
    print(last_patient_wait_time(total_patients=5, time_duration=3))
    print(last_patient_wait_time(total_patients=6, time_duration=5))
    print(last_patient_wait_time(total_patients=7, time_duration=6))
    print(last_patient_wait_time(total_patients=8, time_duration=2))


if __name__ == "__main__":
    main()

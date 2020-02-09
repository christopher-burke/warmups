#!/usr/bin/env python3

"""Convert Number to String of Dashes.

Create a function that takes a number (from 1 - 60) and returns a
corresponding string of hyphens.

Source:
https://edabit.com/challenge/f3jm7sk7LaYttYyLP
"""


def num_to_dashes(n: int) -> str:
    """Create a string of hyphens with length n."""
    return "-" * n


def main():
    """Run sample functions. Do not import."""
    assert num_to_dashes(1) == "-"
    assert num_to_dashes(2) == "--"
    assert num_to_dashes(3) == "---"
    assert num_to_dashes(4) == "----"
    assert num_to_dashes(5) == "-----"
    assert num_to_dashes(6) == "------"
    assert num_to_dashes(7) == "-------"
    assert num_to_dashes(8) == "--------"
    assert num_to_dashes(9) == "---------"
    assert num_to_dashes(10) == "----------"
    assert num_to_dashes(11) == "-----------"
    assert num_to_dashes(12) == "------------"
    assert num_to_dashes(13) == "-------------"
    assert num_to_dashes(14) == "--------------"
    assert num_to_dashes(15) == "---------------"
    assert num_to_dashes(16) == "----------------"
    assert num_to_dashes(17) == "-----------------"
    assert num_to_dashes(18) == "------------------"
    assert num_to_dashes(19) == "-------------------"
    assert num_to_dashes(20) == "--------------------"
    assert num_to_dashes(21) == "---------------------"
    assert num_to_dashes(22) == "----------------------"
    assert num_to_dashes(23) == "-----------------------"
    assert num_to_dashes(24) == "------------------------"
    assert num_to_dashes(25) == "-------------------------"
    assert num_to_dashes(26) == "--------------------------"
    assert num_to_dashes(27) == "---------------------------"
    assert num_to_dashes(28) == "----------------------------"
    assert num_to_dashes(29) == "-----------------------------"
    assert num_to_dashes(30) == "------------------------------"
    assert num_to_dashes(31) == "-------------------------------"
    assert num_to_dashes(32) == "--------------------------------"
    assert num_to_dashes(33) == "---------------------------------"
    assert num_to_dashes(34) == "----------------------------------"
    assert num_to_dashes(35) == "-----------------------------------"
    assert num_to_dashes(36) == "------------------------------------"
    assert num_to_dashes(37) == "-------------------------------------"
    assert num_to_dashes(38) == "--------------------------------------"
    assert num_to_dashes(
        39) == "---------------------------------------"
    assert num_to_dashes(
        40) == "----------------------------------------"
    assert num_to_dashes(
        41) == "-----------------------------------------"
    assert num_to_dashes(
        42) == "------------------------------------------"
    assert num_to_dashes(
        43) == "-------------------------------------------"
    assert num_to_dashes(
        44) == "--------------------------------------------"
    assert num_to_dashes(
        45) == "---------------------------------------------"
    assert num_to_dashes(
        46) == "----------------------------------------------"
    assert num_to_dashes(
        47) == "-----------------------------------------------"
    assert num_to_dashes(
        48) == "------------------------------------------------"
    assert num_to_dashes(
        49) == "-------------------------------------------------"
    assert num_to_dashes(
        50) == "--------------------------------------------------"
    assert num_to_dashes(
        51) == "---------------------------------------------------"
    assert num_to_dashes(
        52) == "----------------------------------------------------"
    assert num_to_dashes(
        53) == "-----------------------------------------------------"
    assert num_to_dashes(
        54) == "------------------------------------------------------"
    assert num_to_dashes(
        55) == "-------------------------------------------------------"
    assert num_to_dashes(
        56) == "--------------------------------------------------------"
    assert num_to_dashes(
        57) == "---------------------------------------------------------"
    assert num_to_dashes(
        58) == "----------------------------------------------------------"
    assert num_to_dashes(
        59) == "-----------------------------------------------------------"
    assert num_to_dashes(
        60) == "------------------------------------------------------------"
    print('Passed.')


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""This script defines a function find_peak to
find a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """This function takes a list of unsorted integers as input
    and returns a peak from the list.It uses a binary search
    approach to find the peak efficiently.
    """

    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
        return list_of_integers[low]

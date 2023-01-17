#!/usr/bin/python3
"""
Find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif list_of_integers[0] >= 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]

    h = len(list_of_integers) - 1
    low = 0
    arr = list_of_integers
    while h > low:
        mid = (h + low) // 2
        if arr[mid] <= arr[mid + 1]:
            low = mid + 1
        elif arr[mid] <= arr[mid - 1]:
            h = mid - 1
        elif arr[mid] >= arr[mid + 1] and arr[mid] >= arr[mid - 1]:
            return arr[mid]
    return arr[low]

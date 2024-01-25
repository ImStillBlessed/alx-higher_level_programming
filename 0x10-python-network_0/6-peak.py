#!/usr/bin/python3
"""
 This is a module for the function find_peak()
 """


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using divide and conquer.
    Returns the peak integer or None if the list is empty.
    """

    if not list_of_integers:
        return None

    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_helper(arr, start, end):
    """
    Helper function for finding peak recursively.
    """
    if start == end:
        return arr[start]

    mid = (start + end) // 2

    if arr[mid] < arr[mid + 1]:
        return find_peak_helper(arr, mid + 1, end)
    else:
        return find_peak_helper(arr, start, mid)

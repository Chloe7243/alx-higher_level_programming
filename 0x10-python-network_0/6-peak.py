#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    loi = list_of_integers
    loil = len(loi)
    if (loil == 0):
        return None
    else:
        i = 0
        while (i + 1 < loil and loi[i + 1] > loi[i]):
            i += 1
    return loi[i]

#!/usr/bin/python3
"""
A script to find the peak in an unsorted list
"""


def find_peak(itg):
    """
    method that finds the peak in a unsorted list
    """
    if itg:
        print(itg)
        if len(itg) == 1:
            return itg[0]
        mid = (len(itg)) // 2
        if itg[mid] < itg[mid - 1]:
            return find_peak(itg[:mid])
        elif itg[mid] < itg[mid + 1]:
            return find_peak(itg[mid + 1:])
        else:
            return itg[mid]

#!/usr/bin/python3
"""
A script to find the peak in an unsorted list
"""

def find_peak(list_of_integers):
    """
    method that finds the peak in a unsorted list
    """
    if (len(list_of_integers) == 1):
        return list_of_integers[1]
    elif (len(list_of_integers) == 0):
        return None
    return list_of_integers[-2]

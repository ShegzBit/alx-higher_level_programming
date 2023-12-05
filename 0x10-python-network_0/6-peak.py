#!/usr/bin/python3
"""
method that finds the in unsorted list
"""


def find_peak(integers):
    """
    method that finds the in unsorted list
    """
    if (len(integers) == 1):
        return integers[0]
    elif (len(integers) == 0):
        return None
    else:
        real_value = None
        fallback = []
        i = 0
        while i < len(integers):
            if i - 1 >= 0 and i + 1 <= len(integers) - 1:
                if (integers[i] > integers[i - 1] and
                        integers[i] > integers[i + 1]):
                    real_value = integers[i]
                    break
            elif i - 1 < 0:
                if integers[i] >= integers[i - 1]:
                    fallback.append(integers[i])
            i += 1

        return (real_value if real_value else fallback[0])

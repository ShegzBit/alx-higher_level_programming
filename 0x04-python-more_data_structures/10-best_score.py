#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    val = 0
    for x, y in a_dictionary.items():
        if y > val:
            val = y
            val_key = x
    return val_key

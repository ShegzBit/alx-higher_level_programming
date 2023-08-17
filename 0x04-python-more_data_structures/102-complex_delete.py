#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    new_dic = {x: y for x, y in a_dictionary.items()}
    for x, y in new_dic.items():
        if y == value:
            del a_dictionary[x]
    return a_dictionary

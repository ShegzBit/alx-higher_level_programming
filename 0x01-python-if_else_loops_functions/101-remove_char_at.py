#!/usr/bin/python3
def remove_char_at(str, n):
    my_list = list(str)
    new_list = []
    str_len = len(str)
    i = 0
    while i < str_len:
        if i != n:
            new_list.append(str[i])
        i += 1
    new_str = "".join(new_list)
    return new_str

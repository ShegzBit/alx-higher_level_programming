#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    i = 0
    new_list = []
    while i < len(my_list):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])
        i += 1
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)

    new_list = replace_in_list(my_list, -1, new_element)

    print(new_list)
    print(my_list)

    new_list = replace_in_list(my_list, 5, new_element)
    print(new_list)
    print(my_list)

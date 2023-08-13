#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1 or my_list is None:
        return my_list
    my_list[idx] = element
    return my_list


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

    new_list = replace_in_list(['a', 2, 'c'], 1, 'd')
    print(new_list)

    print(replace_in_list([1, 2, 2, 3], 2, 4))

    print(replace_in_list([[1, 2], [3, 4]], 1, [5, 6]))
    print(replace_in_list([None, 2, None], 1, 4))

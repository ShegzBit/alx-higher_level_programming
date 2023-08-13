#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            t_1 = (0, 0)
        else:
            t_1 = (tuple_a[0], 0)
    else:
        t_1 = tuple_a[0], tuple_a[1]
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            t_2 = (0, 0)
        else:
            t_2 = (tuple_b[0], 0)
    else:
        t_2 = tuple_b[0], tuple_b[1]
    t_3 = (t_1[0] + t_2[0], t_1[1] + t_2[1])
    return t_3


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)

    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(None, (0, 4, 5, 6)))

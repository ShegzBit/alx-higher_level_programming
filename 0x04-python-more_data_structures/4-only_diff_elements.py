#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    in_set1 = set(x for x in set_1 if x not in set_2)
    in_both_set = set(x for x in set_2 if x not in set_1)
    in_both_set.update(in_set1)
    return in_both_set

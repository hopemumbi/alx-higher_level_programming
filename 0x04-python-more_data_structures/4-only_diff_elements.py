#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """function that returns a set of all elements present in only one set.

    Args:
        set_1: first set
        set_2: second set

    Return:
        elements present only in one set
    """
    # elements present only in one set
    # ^ the symetric difference
    return set_1 ^ set_2

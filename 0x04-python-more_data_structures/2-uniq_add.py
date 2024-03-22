#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list
        (only once for each integer).


    Args:
        my_list: a list of integers

    Return:
        The sum
    """
    new_list = list(set(my_list))
    sum = 0
    for i in new_list:
        sum = sum + i
        return sum

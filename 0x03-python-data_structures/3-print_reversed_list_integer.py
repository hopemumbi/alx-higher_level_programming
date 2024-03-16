#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order.

    Args:
        my_list: List to be reversed
    """
    # check if list is empty
    if len(my_list) != 0:
        # if not make a copy
        new_list = my_list.copy()
        # reverse the new string
        my_list.reverse()
        # iterate through the new list
        for i in range(len(new_list)):
            # print one integer per line
            print("{:d}".format(new_list[i]))

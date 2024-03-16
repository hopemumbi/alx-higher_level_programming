#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order.

    Args:
        my_list: List to be reversed
    """
    # reverse the list
    my_list.reverse()
        # iterate through the new list
        for i in range(len(my_list)):
            # print one integer per line
            print("{:d}".format(my_list[i]))

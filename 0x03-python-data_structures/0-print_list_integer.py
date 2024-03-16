#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """function that prints all integers of a list.
    Args:
        my_list=[] - the list of integers
    """
    for n in my_list:
        # use str.format() to print integers
        print("{}".format(n))

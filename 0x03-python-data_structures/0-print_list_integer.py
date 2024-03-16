#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """function that prints all integers of a list.

    Args:
        my_list=[]: The list of integers

    """
    # Iterate over the indices of the list
    for i in my_list:
        # use str.format() to print integers at the current index i of my_list.
        print("{}".format(i))

#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """function that prints all integers of a list.

    Args:
        my_list=[]: The list of integers

    """
    # Iterate over the indices of the list
    for i in range(len(my_list)):
        # output one integer per line
        print("{:d}".format(my_list[i]))

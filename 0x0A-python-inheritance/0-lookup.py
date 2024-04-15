#!/usr/bin/python3
def lookup(obj):
    """ function that returns the list of
    available attributes and methods of an object:
    Args:
        obj: The instance to be listed
    """
    # Create an empty list to store the attributes and methods
    lst = []

    # Use a dictionary to access the key for each attributes and method
    for name in obj.__dict__.keys():
        # Append the key to the list
        lst.append(name)
    # Return the list of attributes and methods
    return lst

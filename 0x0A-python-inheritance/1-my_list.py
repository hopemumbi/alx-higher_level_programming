#!/usr/bin/python3
""" Module that demonstrate inheritance of classes"""


class MyList(list):
    """Inherits from the builtin class `list` """
    # Constructor
    def __init__(self, *args):
        """Initializes every instance of the class(`MyLIst`)

        Args:
            *args: any number of positional argument
        """
        # Calls the constructor of the parent class (list)
        super().__init__()

    def print_sorted(self):
        """ Print a sorted copy of the list"""
        print(sorted(self))

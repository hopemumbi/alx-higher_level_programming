#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Print integer followed by a new line
        print("{:d}".format(value))
        # Return True if value is an integer
        return True
    except (TypeError, ValueError):
        # Return False if value is not an integer
        return False

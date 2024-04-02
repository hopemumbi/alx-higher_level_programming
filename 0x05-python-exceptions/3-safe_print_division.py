#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # Divide 2 integers
        result = a / b
    except ZeroDivisionError:
        # Handle when denom is 0
        result = None
    finally:
        # print the result
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
    return result

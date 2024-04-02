#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Initialize an empty list
    result = []

    try:
        # Iterate through both lists
        for i in range(list_length):
            # Try to divide elements at index i
            try:
                result.append(my_list_1[i] / my_list_2[i])
            # Check if the division can’t be done (/0)
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
            # Check if an element is not an integer or float
            except TypeError:
                result.append(0)
                print("wrong type")
            # Check if my_list_1 or my_list_2 is too short
            except IndexError:
                print("out of range")
    # Return a new list (length = list_length) with all divisions
    finally:
        return result

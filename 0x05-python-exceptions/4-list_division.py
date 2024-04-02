#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Initialize a new list
    new_list = [0]*list_length
    # Iterate through both lists
    for i in range(list_length):
        # initialize result to 0
        result = 0
        # Try to divide elements at index i
        try:
            result = (my_list_1[i] / my_list_2[i])
        # Check if the division can’t be done (/0)
        except ZeroDivisionError:
            print("division by 0")
        # Check if an element is not an integer or float
        except TypeError:
            print("wrong type")
        # Check if my_list_1 or my_list_2 is too short
        except IndexError:
            print("out of range")
        # Assign the result or 0  to new_list[i]
        finally:
            new_list[i] = result

    # Return a new list (length = list_length) with all divisions
    return new_list

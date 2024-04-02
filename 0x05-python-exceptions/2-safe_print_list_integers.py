#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        # Iterate through my_list up to x
        for i in range(x):
            # Check if the element is an integer
            if isinstance(my_list[i], int):
                # print only integers on the same line
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except (ValueError, TypeError):
        pass
    else:
        # print a new line
        print()
        # return the number of elements printed
        return count

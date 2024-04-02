#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        # Iterate through my_list up to x
        for i in range(x):
            # print only integers on the same line
            print(my_list[i], end="")
            count += 1
    except (IndexError, TypeError):
        pass
    else:
        # print a new line
        print()
    # return the number of elements printed
    return count

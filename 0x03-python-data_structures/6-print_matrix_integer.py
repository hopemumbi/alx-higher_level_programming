#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers.

    Args:
        matrix: matrix of integers to be printed
    """
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each element in the row
        for i in range(len(row)):
            # Check if it's the last element in the row
            if i == (len(row) - 1):
                # If it is, print it without a space at the end
                print("{:d}".format(row[i]), end="")
            else:
                # If it's not  print it with a space at the end
                print("{:d}".format(row[i]), end=" ")
        # Move to the next line after printing all elements in the row
        print("")

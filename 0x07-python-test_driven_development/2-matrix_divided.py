#!/usr/bin/python3
"""Module for matrix division"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.
    Args:
        matrix (list of lists): the  matrix to be divided
        div (int or float): the divisor

    Returns:
        list of lists: a new matrix with all elements divided by the divisor
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    # matrix must be a list of lists of integers or floats
    if not isinstance(matrix, list):
        raise TypeError(message)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)

    if not all(
        isinstance(elem, (int, float)) and not isinstance(elem, bool)
        for row in matrix
        for elem in row
    ):
        raise TypeError(message)

    # Each row of the matrix must be of the same size
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # div must be a number (integer or float),
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    # div can’t be equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # divide each element of the matrix by div
    result = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

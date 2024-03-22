#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function that squares of a matrix.


    Args:
        matrix: matrix to be squared

    Return:
        the squared matrix
    """
    s_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return s_matrix

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ function that adds 2 tuples.

    Args:
        tuple_a: first tuple
        tuple_b: second tuple
    """
    # find the length of each tuple
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    # check if  tuple_a is smaller than 2 then
    if len_a < 2:
        # fill it with zeros
        tuple_a = tuple_a + (0, 0)

    # check if  tuple_b is smaller than 2 then
    if len_b < 2:
        # fill it with zeros
        tuple_b = tuple_b + (0, 0)
    # check if  tuple_a is smaller than 2 then
    tuple_b = tuple_b + (0, 0)

    # calculae the sum of the first 2 elements
    sum_0 = tuple_a[0] + tuple_b[0]
    # calculate the sum of the second 2 elements
    sum_1 = tuple_a[1] + tuple_b[1]

    return (sum_0, sum_1)

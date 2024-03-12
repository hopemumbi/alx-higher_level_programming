#!/usr/bin/python3
def print_last_digit(number):
    # prints the last digit of a number.
    # use the modulus of 10 to find the last digit
    # handle negative numbers
    if number < 0:
        print('{:d}'.format(-number % 10))
    else:
        print('{:d}'.format(number % 10))

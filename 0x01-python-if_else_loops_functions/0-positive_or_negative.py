#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# check if number is positive
if (number > 0):
    print('{} is positive'.format(number))
# check if number is zero
elif (number == 0):
    print('{} is zero'.format(number))
# check if number is negative
elif (number < 0):
    print('{} is negative'.format(number))

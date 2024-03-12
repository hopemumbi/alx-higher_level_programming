#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#find the last digit of a number
if number < 0:
    last_digit = (number * -1) % 10
else:
    last_digit = number % 10

#if the last digit is greater than 5
if (last_digit > 5):
    print('Last digit of {} is {} and is greater than 5'.format(number, last_digit))

#if the last digit is 0
elif (last_digit == 0):
    print('Last digit of {} is {} and is 0'.format(number, last_digit))

#if the last digit is less than 6 and not 0
elif (last_digit < 6) and (last_digit != 0):
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, last_digit))

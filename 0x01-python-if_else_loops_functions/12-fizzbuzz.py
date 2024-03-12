#!/usr/bin/python3
def fizzbuzz():
    # prints the numbers from 1 to 100 separated by a space.
    for i in range(1, 101):
        # multiples of both three and five print FizzBuzz
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=" ")
        # multiples of three print Fizz
        elif i % 3 == 0:
            print('Fizz', end=" ")
        # multiples of five print Buzz
        elif i % 5 == 0:
            print('Buzz', end=" ")
        else:
            print('{}'.format(i), end=" ")

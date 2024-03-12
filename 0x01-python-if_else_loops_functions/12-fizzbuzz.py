#!/usr/bin/python3
def fizzbuzz():
    # prints the numbers from 1 to 100 separated by a space.
    for i in range(1, 101):
        # multiples of three print Fizz
        if i % 3 == 0:
            print('Fizz', end=" ")
        # multiples of five print Buzz
        elif i % 5 == 0:
            print('Buzz', end=" ")
        # multiples of both three and five print FizzBuzz
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=" ")
        else:
            print('{}'.format(i), end=" ")

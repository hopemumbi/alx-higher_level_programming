#!/usr/bin/python3

# ensure code is not executed when imported
if __name__ == "__main__":
    # import calculator_1 module
    from calculator_1 import add, sub, mul, div

    # set variables a and b
    a = 10
    b = 5

    # output addition
    print("{} + {} = {}".format(a, b, add(a, b)))
    # output subtraction
    print("{} - {} = {}".format(a, b, sub(a, b)))
    # output multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))
    # outpu division
    print("{} / {} = {}".format(a, b, div(a, b)))

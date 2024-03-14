#!/usr/bin/python3
# ensure code is not executed when imported
if __name__ == "__main__":
    # import module
    from calculator_1 import add, sub, mul, div
    # set variables
    a = 10
    b = 5
    # output addition
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    # output subtraction
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    # output multiplication
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    # output division
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

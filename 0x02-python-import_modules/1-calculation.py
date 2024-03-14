#!/usr/bin/python3

# ensure code is not executed when imported
if __name__ == "__main__":
    # import calculator_1 module
    from calculator_1 import add, sub, mul, div

    # set variables a and b
    a = 10
    b = 5

    # print addition
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    # print subtraction
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    # print multiplication
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    # print division
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

#!/usr/bin/python3

# ensure code is not executed when imported
if __name__ == "__main__":
    # import calculator_1 module
    from calculator_1 import add, sub, mul, div

    # set variables a and b
    a = 10
    b = 5

    # output addition
    print(a, "+", b, "=", add(a, b))
    # output subtraction
    print(a, "-", b, "=", sub(a, b))
    # output multiplication
    print(a, "*", b, "=", mul(a, b))
    # output division
    print(a, "/", b, "=", div(a, b))

#!/usr/bin/python3
# import calculator_1 module
from calculator_1 import add, sub, mul, div
# set variables a and b
a = 10
b = 5
# ensure code is not executed when imported
if __name__ == "__main__":
    # print addition
    print(f"{a} + {b} = {add(a, b)}")
    # print subtraction
    print(f"{a} - {b} = {sub(a, b)}")
    # print multiplication
    print(f"{a} * {b} = {mul(a, b)}")
    # print division
    print(f"{a} / {b} = {div(a, b)}")

#!/usr/bin/python3
if __name__ == "__main__":
    # import sys module
    from sys import argv

    # variable argc = number of args
    argc = len(argv) - 1
    # if number of args == 1 then
    if argc == 1:
        # print Number of argument(s) followed by argument
        print(argc, "argument:")
    # else if argc == 0
    elif argc == 0:
        print(argc, "arguments.")
    # else
    else:
        # print Number of argument(s) followed by arguments
        print(argc, "arguments:")
    # initialize a variable i to 1;
    i = 1
    # while  i <= argc then
    while i <= argc:
        # print the <argument vector>  :, <argument value> and a new line
        print(i, ":", argv[i])
        # increment i to move to the next argument
        i += 1

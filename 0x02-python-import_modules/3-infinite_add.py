#!/usr/bin/python3
# ensure code should not be executed when imported
if __name__ == "__main__":
    # import sys/argv module
    from sys import argv
    # initialize sum to 0
    sum = 0
    # use a loop to iterate through the arguments
    for i in range(1, len(argv)):
        # cast the arguments to integers and add them to the sum
        sum += int(argv[i])
    # print the sum
    print("{}".format(sum))

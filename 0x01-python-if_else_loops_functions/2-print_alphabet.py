#!/usr/bin/python3
# use one loop to print the ASCII alphabet
for alpha in range(97, 123):
    # print, not followed by a new line
    print("{}".format(chr(alpha)), end="")

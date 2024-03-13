#!/usr/bin/python3
# use only one loop to  print the ASCII alphabet
# reverse the alphabet
for i in range(122, 96, -1):
    # print the the alphabet while
    # alternate lowercase and uppercase
    # not followed by a new line
    if i % 2 == 0:
        print('{}'.format(chr(i)), end="")
    # convert the lowercase to uppercase
    else:
        print('{}'.format(chr(i - 32)), end="")

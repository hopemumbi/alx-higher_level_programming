#!/usr/bin/python3
# use one loop to print the ASCII alphabet
for alpha in range(97, 123):
    # exclude 'q' and 'e'
    if alpha != 101 and alpha != 113:
        # print, not followed by a new line
        print("{:c}".format(alpha), end="")

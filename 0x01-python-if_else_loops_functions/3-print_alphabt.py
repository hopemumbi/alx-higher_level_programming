#!/usr/bin/python3
# use one loop to print the ASCII alphabet
for alpha in range(97, 123):
    # exclude 'q' and 'e'
    if chr(alpha) != 'q' and chr(alpha) != 'e':
        #print, not followed by a new line
        print("{}".format(chr(alpha)), end="")

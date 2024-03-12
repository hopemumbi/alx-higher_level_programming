#!/usr/bin/python3
#Use for to loop through the lowercase ASCII range
for alphabet in range(97, 123):
    #print the ASCII alphabet, not followed by a new line.
    print('{:c}'.format(alphabet), end="")

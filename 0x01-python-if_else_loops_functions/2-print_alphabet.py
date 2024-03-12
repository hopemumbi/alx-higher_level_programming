#!/usr/bin/python3
# Use only one loop
for c in range(123):
    if (c >= 97) and (c <= 122):
        # print the ASCII alphabet, not followed by a new line.
        print('{:c}'.format(c), end="")

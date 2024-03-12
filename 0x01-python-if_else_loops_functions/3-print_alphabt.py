#!/usr/bin/python3
# use for loop through the alphabet
for c in range(97, 123):
    # Use if statement to omit 'q' and 'e'
    if (c == 101) or (c == 113):
        continue
    # print ASCII alphabet not followed by a new line.
    print('{:c}'.format(c), end="")

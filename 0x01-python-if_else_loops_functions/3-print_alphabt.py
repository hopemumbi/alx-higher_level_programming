#!/usr/bin/python3
# use for loop through the alphabet
for c in range(97, 123):
    # Use if statement to omit 'q' and 'e'
    if c not in [101, 113]:
        # print ASCII alphabet not followed by a new line.
        print('{:c}'.format(c), end="")

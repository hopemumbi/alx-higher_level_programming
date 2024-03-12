#!/usr/bin/python3
#use for loop through the alphabet
for alphabet in range(97, 123):
    #Use if statement to omit 'q' and 'e'
    if ((alphabet != 101) and (alphabet != 113)):
        #print ASCII alphabet not followed by a new line.
        print('{:c}'.format(alphabet), end="")

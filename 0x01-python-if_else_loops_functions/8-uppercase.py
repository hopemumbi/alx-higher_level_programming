#!/usr/bin/python3
def uppercase(str):
    # iterate over each character in str
    for i in str:
        # check if the character is lowercase
        if (ord(i) >= 97 and ord(i) <= 122):
            # convert the lowercase to uppercase
            i = chr(ord(i) - 32)
        # output the character either coverted or otherwise
        print('{}'.format(i), end="")
    # add a newline at the end
    print()

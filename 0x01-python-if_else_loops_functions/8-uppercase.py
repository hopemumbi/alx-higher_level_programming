#!/usr/bin/python3
def uppercase(str):
    # iterate over each character in str
    for i in str:
        # check if the character is lowercase
        if (ord(i) >= 97 and ord(i) <= 122):
            # convert the lowercase to uppercase
            i = chr(ord(i) - 32)
        # print the charaster either coverted or otherwise
        print('{}'.format(i), end="")
    # print a newline at the end
    print()

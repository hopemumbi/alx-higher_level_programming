#!/usr/bin/python3
# use only one loop from 0 to 99
for number in range(0, 100):
    # print separated by comma in ascending order, with two digits
    if number < 99:
        print('{:02d}'.format(number), end=", ")
    # omit comma at the end
    else:
        print('{}'.format(number))

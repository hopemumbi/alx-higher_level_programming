#!/usr/bin/python3
# use for to loop from 0 to 99
for number in range(100):
    if (number < 99):
        continue
        # print separated by comma in ascending order, with two digits
        print('{:02d}'.format(number), end=", ")
    else:
        # omit comma at the end
        print('{:02d}'.format(number))

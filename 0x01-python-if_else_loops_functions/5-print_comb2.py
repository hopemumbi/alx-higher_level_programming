#!/usr/bin/python3
# use for to loop from 0 to 99
for number in range(0, 100):
    # omit comma at the end
    if number == 99:
        print('{}'.format(number))
    # print separated by comma in ascending order, with two digits
    else:
        print('{:02d}'.format(number), end=", ")

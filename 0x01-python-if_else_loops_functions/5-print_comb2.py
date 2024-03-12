#!/usr/bin/python3
# use for to loop from 0 to 99
for number in range(0, 99):
    # print separated by comma in ascending order, with two digits
    print('{:02d}'.format(number), end=", ")
# omit comma at the end
print('99')

#!/usr/bin/python3
# prints all possible different combinations of two digits
for i in range(0, 10):
    # initialilize witn i so 01 and 10 are the same combination
    for j in range(i, 10):
        # the two digits must be different
        if (i != j):
            # print in ascending order
            print('{}{}'.format(str(i), str(j)), end=", ")
            # last number should be followed by a new line
            if (i + j == 17):
                print('{}{}'.format(str(i), str(j)))

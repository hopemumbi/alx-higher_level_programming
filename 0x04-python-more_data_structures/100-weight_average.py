#!/usr/bin/python3
def weight_average(my_list=[]):
    # check if list is empty
    if my_list == []:
        return 0
    else:
        # create an empty list
        new_list = []
        # iterate through the list then
        for tup in my_list:
            # convert each tuple to a list and add it to new_list
            new_list.append(list(tup))

        # calculate the numerator
        numerator = sum([score * weight for score, weight in new_list])
        # calculte the denominator
        denominator = sum([weight for _, weight in new_list])
        # return the weighted average
        weighted_average = numerator / denominator
        return weighted_average

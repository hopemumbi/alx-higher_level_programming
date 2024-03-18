#!/usr/bin/python3
def multiple_returns(sentence):
    """function returns tuple -length of a string, its first character.

    Args:
        sentence: string to be analyzed

    Return:
        length of a string, its first character.
    """
    # check if sentence is empty then
    if len(sentence) == 0:
        # the first character should be equal to None
        r_tuple = len(sentence), None
    else:
        # set the tuple with  length of the sentence, its first character
        r_tuple = len(sentence), sentence[0]
    # return the tuple
    return r_tuple

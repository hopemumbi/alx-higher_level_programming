#!/usr/bin/python3
"""Module for printing a text"""


def text_indentation(text):
    """prints a text
    with 2 new lines after each of these characters: ., ? and :
    no space at the beginning or at the end of each printed line

    Args:
        text (str): the rest to be printed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Initialize an empty string
    n_text = ""
    # Create a flag to skip spaces
    skip_spaces = True
    # Iterate through the text
    for i in range(len(text)):
        # If the current character is " "
        # and skip_spaces = True then
        if text[i] == " " and skip_spaces:
            # continue to the next iteration
            continue
        # Spaces should be included
        skip_spaces = False
        # Add current character to n_text
        n_text += text[i]
        # Check if current character is in [".", "?", ":"]:
        if text[i] in [".", "?", ":"]:
            # Then add 2 new lines
            n_text += "\n\n"
            # Set skip_spaces = True to skip adding spaces to next line
            skip_spaces = True
    # Print the new line
    print(n_text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

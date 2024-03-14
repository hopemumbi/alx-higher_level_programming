#!/usr/bin/python3
# Check if the script is being run as the main program
if __name__ == "__main__":
    # Import the hidden_4 module
    import hidden_4
    # Get a list of names defined in hidden_4
    names = dir(hidden_4)
    # Iterate over each name in the list
    for i in names:
        # Check if the name does not start with "__"
        if i[0:2] != "__":
            # Print the name
            print(i)

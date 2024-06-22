# print("abhishek")


# import six (cntl+ /) --> to comment any things

"""hey this 
is multiline comment
"""
import os

def print_directory_contents(sPath):
    """
    This function prints the contents of a directory recursively.
    """
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

# Call the function to print the contents of the current working directory
print_directory_contents(".")



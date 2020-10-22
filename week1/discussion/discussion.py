"""
This just lets you type in a string and then prints it out in a diagonal
line. If one of the characters is "W" then there will be one additional
space before the following character.
"""
def main():
    """
    This function exists solely so pylint does not flag 'space' as a
    constant
    """
    name = input("Name: ")
    space = " "

    for char in name:
        print(space, char)
        if char == "W":
            space += "  "
        else:
            space += " "

main()

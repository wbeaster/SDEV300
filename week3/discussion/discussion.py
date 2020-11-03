"""
This is here to illustrate using Python exceptions
"""

from decimal import Decimal

#original function
#just here for reference
def right_circular_cylinder_column_menu():
    """
    Asks the user for cylinder radius and cylinder height
    """
    radius = None
    height = None

    while not radius:
        radius = input("Radius (must be a positive number: ")
        if not radius.isdecimal():
            radius = None
        elif not Decimal(radius) > 0:
            radius = None
    radius = Decimal(radius)

    while not height:
        height = input("Height (must be a positive number): ")
        if not height.isdecimal():
            height = None
        elif not Decimal(height) > 0:
            height = None
    height = Decimal(height)

    return radius, height

#this function uses exceptions
def e_right_circular_cylinder_column_menu():
    """
    Asks the user for cylinder radius and cylinder height
    Using exceptions for input checking
    """
    radius = None
    height = None

    while not radius:
        try:
            radius = int(input("Radius (must be a positive integer): "))
            if radius > 0:
                break
            print("You must enter a positive integer.")
            radius = None
        except ValueError:
            print("You must enter a positive integer.")
    radius = Decimal(radius)

    while not height:
        try:
            height = int(input("Height (must be a positive integer): "))
            if height > 0:
                break
            print("You must enter a positive integer.")
            height = None
        except ValueError:
            print("You must enter a positive integer.")
    height = Decimal(height)

    return radius, height

args = e_right_circular_cylinder_column_menu()

print(args)

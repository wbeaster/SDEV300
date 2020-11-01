"""
Lab2

Create a menu-driven python application with following menu options for
users to run at the command line:
a.Generate Secure Password
b.Calculate and Format a Percentage
c.How many days from today until
July 4, 2025?
d.Use the Law of Cosines to calculate the leg of a triangle.
e.Calculate the volume of a Right Circular Cylinder
f.Exit program
"""

from decimal import Decimal
from datetime import date
#I wish I understood why pylint has an issue with pi
#Workaround is to import math
#from math import cos, pi, sqrt
import math
import secrets
import string

MAIN_MENU_CHOICES = ['a', 'b', 'c', 'd', 'e', 'f']
YES = ['Y', 'YES']
NO = ['N', 'NO']

def display_banner():
    """Displays the welcome/identifying banner"""
    print('***SDEV300 7384 Lab: Math and Secret Generation***')
    print('***William Easter')

def display_main_menu():
    """Dispalys the main menu"""
    print('a. Generate Secure Password')
    print('b. Calculate and Format a Percentage')
    print('c. How many days from today until July 4, 2025?')
    print('d. Use the Law of Cosines to calculate the leg of a triangle.')
    print('e. Calculate the volume of a Right Circular Cylinder')
    print('f. Exit program')

def get_choice_main_menu():
    """
    Solicits the user's choice from the menu
    Only allows valid choices
    """
    choice = None
    while choice not in MAIN_MENU_CHOICES:
        choice = input("Choice (a - f): ").lower()
    return choice

def get_yes_no(prompt):
    """
    This exists solely because the linter says there are too many branches
    in generate_secure_password_nmenu()
    Expects a string to be used as the prompt
    Tests to make sure the user enters some thing in YES or NO
    Returns_______
    """
    response = None

    while not response:
        response = input(prompt).upper()

        if response not in YES and response not in NO:
            response = None

    return response

def generate_secure_password_menu():
    """
    Dispalys password options to the user and allows them to select
    their password complexity
    """
    length = None
    use_upper_case = None
    use_lower_case = None
    use_numbers = None
    use_specials = None

    while not length:
        length = input('Password length (must be positive integer): ')
        if not length.isdigit():
            length = None
        elif int(length) < 1:
            length = None
    length = int(length)

    while not (use_lower_case or use_upper_case or use_numbers or use_specials):

        use_lower_case = get_yes_no('Use lower case letters? (y/n) ') in YES

        use_upper_case = get_yes_no('Use upper case letters? (y/n) ') in YES

        use_numbers = get_yes_no('Use numbers? (y/n) ') in YES

        use_specials = get_yes_no('Use specials? (y/n) ') in YES

        if not (use_lower_case or use_upper_case or use_numbers or use_specials):
            print('You must select at least one complexity (lower case, upper case, numbers, ' +
                  'specials characters).')

    return length, use_lower_case, use_upper_case, use_numbers, use_specials

def generate_secure_password(args):
    """This function generates a password based on the parameters"""

    #first, unpack the tuple
    length, use_lower_case, use_upper_case, use_numbers, use_specials = args

    #next, we determine what our alphabet is
    alphabet = ''
    if use_lower_case:
        alphabet += string.ascii_lowercase
    if use_upper_case:
        alphabet += string.ascii_uppercase
    if use_numbers:
        alphabet += string.digits
    if use_specials:
        alphabet += string.punctuation

    #now, generate and return the password
    #this is based on the recipe/best practice straight from the
    #python.org documentations:
    #https://docs.python.org/3/library/secrets.html

    return ''.join(secrets.choice(alphabet) for i in range(length))

def calculate_and_format_percentage_menu():
    """
    Allows the user to input their numerator, denominator, and how many
    deimals points to display
    """
    numerator = None
    denominator = None
    decimals = None

    print("Welcome to the Calculate and Format percetnage module.")
    print("You will enter a numerator, denominator, and how many decimals")
    print("you would like to display")
    print("The program will then calculate and display your number")
    print("If needed the program will round your number to the requested")
    print("decimal place.")

    while not numerator:
        numerator = input("Numerator (most be a number): ")
        if not numerator.isdecimal():
            numerator = None
    numerator = Decimal(numerator)

    while not denominator:
        denominator = input("Denominator (most be a non-zero number): ")
        if not denominator.isdecimal():
            denominator = None
        elif denominator == 0:
            denominator = None
    denominator = Decimal(denominator)

    while not decimals:
        decimals = input("Number of decimals to display: ")
        if not decimals.isdigit():
            decimals = None
        elif int(decimals) < 0:
            decimals = None
    decimals = int(decimals)

    return numerator, denominator, decimals

def calculate_and_format_percentage(args):
    """
    Calculates and formats a percentage based on the parameters passed
    Returns a print ready string
    """
    numerator, denominator, decimals = args

    #print(f"Debug data {number}")
    #took a lot of teeth gnashing but the below link showed me the best
    #way to deal with any Python float/rounding issues
    #note that Decimal is imported above
    #https://www.programiz.com/python-programming/methods/built-in/round
    number = Decimal(numerator/denominator)
    number = str(round(number * 100, decimals)) + '%'

    return number

def days_until_20250704():
    """
    Displays the number of days from today until 4 Jul, 2025
    Assumes local timezone
    """

    #since the specificaion has the date hard coded no, effort has been
    #made to generalizethis function in the name of foregoing premature
    #optimization.
    target_day = date(2025, 7, 4)
    today = date.today()
    return (target_day - today).days

def cosine_leg_menu():
    """
    Asks the user for opposite angle, hypotnuse, and leg
    Then calculates the length of the missing triangle piece
    """

    #Credit to KhanAcademy for answering a Pythagorean Theorem vs
    #Law of cosines question I had
    #https://youtu.be/ZElOxG7_m3c

    side_a = None
    side_b = None
    opposite_angle = None

    while not side_a:
        side_a = input("Side A (must be a positive integer): ")
        if not side_a.isdecimal():
            side_a = None
        elif not Decimal(side_a) > 0:
            side_a = None
    side_a = Decimal(side_a)

    while not side_b:
        side_b = input("Side B (must be a positive integer): ")
        if not side_b.isdecimal():
            side_b = None
        if not Decimal(side_b) > 0:
            side_b = None
    side_b = Decimal(side_b)

    while not opposite_angle:
        opposite_angle = input("Opposite angle in radians (must be a positive integer < 180): ")
        if not opposite_angle.isdecimal():
            opposite_angle = None
        elif not Decimal(opposite_angle) > 0 and not Decimal(opposite_angle) < 180:
            opposite_angle = None
    opposite_angle = Decimal(opposite_angle)

    return side_a, side_b, opposite_angle

def cosine_leg(args):
    """
    Calculates a cosine leg using the Law of Cosines based on the inputs
    Law of Cosines: c^2 = a^2 + b^2 - 2ab cos(C) where a, b, and c are
                    sides and C is the angle opposite of c in radians
    Inputs are assumed to be valid Decimals
    Returns an unrounded Decimal
    """

    side_a, side_b, opposite_angle = args

    cos_deg = Decimal(math.cos(opposite_angle))

    side_c2 = (side_a ** 2) + (side_b ** 2) - ((2 * side_a * side_b) * cos_deg)
    side_c = side_c2.sqrt()

    return side_c

def right_circular_cylindar_column_menu():
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

def right_circular_cylindar_column(args):
    """
    Calculates the volume of a right cylinder based on (π*r^2) × height
    Expects radius and height as Decimals
    Returns a Decimal of the volume
    """
    radius, height = args

    return Decimal((Decimal(math.pi) * radius ** 2) * height)

def main():
    """This is the main loop for the application"""
    display_banner()

    choice = None

    while choice != 'f':

        display_main_menu()
        choice = get_choice_main_menu()

        if choice == 'a':
            password_args = generate_secure_password_menu()
            password = generate_secure_password(password_args)
            print(f'Your password is: {password}')
        elif choice == 'b':
            percentage_args = calculate_and_format_percentage_menu()
            percentage = calculate_and_format_percentage(percentage_args)
            print(f'Your percentge is: {percentage}')
        elif choice == 'c':
            days = days_until_20250704()
            print(f'Days until July 4, 2025: {days}')
        elif choice == 'd':
            cosine_leg_args = cosine_leg_menu()
            leg = cosine_leg(cosine_leg_args)
            print(f'The length of leg C is: {leg}')
        elif choice == 'e':
            cylinder_args = right_circular_cylindar_column_menu()
            cylinder_volume = right_circular_cylindar_column(cylinder_args)
            print(f'The cyclinder\'s volume is: {cylinder_volume}')
        elif choice == 'f':
            print("Thank you for using this application")

main()

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
import secrets
import string
import sys

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
        choice = input("Choice (a - f): ")
    return choice

def dispatch(choice):
    """
    Function is passed a valid choice and then call the appropriate
    function
    """
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
        cosine_leg()
    elif choice == 'e':
        right_circular_cylindar_colume()
    elif choice == 'f':
        print("Thank you for using this application")
        sys.exit()

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

    while not use_lower_case:
        use_lower_case = input('Use lower case letters? (y/n) ').upper()

        if use_lower_case not in YES and use_lower_case not in NO:
            use_lower_case = None

    if use_lower_case in YES:
        use_lower_case = True
    else:
        use_lower_case = False

    while not use_upper_case:
        use_upper_case = input('Use upper case letters? (y/n) ').upper()

        if use_upper_case not in YES and use_upper_case not in NO:
            use_upper_case = None

    if use_upper_case in YES:
        use_upper_case = True
    else:
        use_upper_case = False

    #BUG: entering 'y' resolves to False
    while not use_numbers:
        use_numbers = input('Use numbers? (y/n) ')

        if use_numbers.upper() not in YES and use_numbers.upper() not in NO:
            use_numbers = None

    if use_numbers in YES:
        use_numbers = True
    else:
        use_numbers = False

    #BUG: entering 'y' resolves to False
    while not use_specials:
        use_specials = input('Use specials? (y/n) ')

        if use_specials.upper() not in YES and use_specials.upper() not in NO:
            use_specials = None

    if use_specials in YES:
        use_specials = True
    else:
        use_specials = False

    #TODO: What is the user select a length, but no upper/lower/digits/specials

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
    """Displays the number of days from today until 4 Jul, 2025"""
    """Assumes local timezone"""
    
    #since the specificaion has the date hard coded no, effort has been
    #made to generalizethis function in the name of foregoing premature
    #optimization.
    target_day = date(2025, 7, 4)
    today = date.today()
    return (target_day - today).days

def cosine_leg():
    """
    Asks the user for opposite angle, hypotnuse, and leg
    Then calculates the length of the missing triangle piece
    """
    return

def right_circular_cylindar_colume():
    """
    Asks the user for cylinder radiu and cylinder height
    Calculates the volume base on (π*r^2) × Height
    """
    return






def main():
    """This is the main loop for the application"""
    display_banner()
    display_main_menu()
    choice = get_choice_main_menu()
    dispatch(choice)





main()



def get_phone():
    print('Please enter your phone number in this form:')
    print('XXX-XXX-XXXX')
    number = input()

    return number

def get_zip4():
    print('Please enter your ZIP+4 in this form:')
    print('XXXXX-XXXX')
    zip4 = input()

    return zip4

def get_matrix():

    #Show the matrix grid, including the column and row IDs
    #Then:
    #   Enter A1
    #   Enter A2
    #      ...
    #   Enter C3
    #Allow Decimals

    print('This is what your 3 x 3 matrix looks like:')
    print('   1   2   3')
    print('A  x   x   x')
    print('B  x   x   x')
    print('C  x   x   x')
    print('You will be asked to input your matrix one element at a time.')
    print('Inputs must be numbers')
    

    return

def handle_phone():
    phone_number = None

    while not is_valid_phone(phone_number):
        phone_number = get_phone()

    return

def handle_zip4():
    zip4 = None

    while not is_valid_zip4(zip4):
        zip4 = get_zip4()

    return

def handle_matrix()
    valid_matrix = False
    matrix = None

    while not valid_matrix:
        



def is_valid_phone(number):
    #TODO: Do the regex thing here

    return

def is_valid_zip4(zip4):
    #TODO: Do the regext hing here
    return

def main_menu():
    choice = None

    while choice != 4:
        print('***Welcome to Lab 4: Phones, ZIPs, and matrices***')
        print('1. Validate phone number')
        print('2. Validate ZIP+4')
        print('3. Matrix math')
        print('4. Exit')
        input('Please enter a number (1-4): ')

        if choice == '1':
            handle_phone()
        elif choice == '2':
            handle_zip4()
        elif choice == '3':
            handle_matrix()
        elif choice == '4':
            print("Thank you for using this application")

    return

def main():
    main_menu()
    return
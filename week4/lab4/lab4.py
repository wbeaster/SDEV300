"""
Lab3 allows auser to enter and validatetheir phone number and zipcode+4. Then
the user will entervalues of two, 3x3 matrices and then select from options
including, addition, subtraction, matrix multiplication, and element by element
multiplication. You should use numpy.matmul()for matrix multiplication (e.g.
np.matmul(a, b)).The program should computethe appropriate results and return
the results, the transpose of the results, the mean of the rows for the
results, and the mean of the columns for the results.
"""

import re
import numpy as np

REGEX_PHONE = r"\d{3}-\d{3}-\d{4}"
REGEX_ZIP4 = r"\d{5}-\d{4}"

def get_phone():
    """
    Parameters: None

    Returns: A number which may or may not be a valid phone number
    """
    print('Please enter your phone number in this form:')
    print('XXX-XXX-XXXX')
    number = input()

    return number

def get_zip4():
    """
    Parameters: None

    Returns: A number which may or may not be a valid zip+4
    """
    print('Please enter your ZIP+4 in this form:')
    print('XXXXX-XXXX')
    zip4 = input()

    return zip4

def get_row(num):
    """
    Parameters: num, which is the number of the row that will be displayed
    to the user

    Returns: A list of three floats
    """
    row = None
    while not row:
        row = input(f"Matrix row {num}: ")
        row = row.split()
        if len(row) != 3:
            row = None
        else:
            for element in row:
                try:
                    element = float(element)
                except ValueError:
                    row = None
    return row

def get_matrices():
    """
    Parameters: None

    Returns: A tuple of two 3x3 matrices of floats
    """

    print("Please enter two matrices.")
    print("The entries will be one row at a time.")
    print("The elements will be seperated by spaces.")
    print("Entries must be a real number.")

    print("This is for matrix 1:")
    row1 = get_row(1)
    row2 = get_row(2)
    row3 = get_row(3)
    matrix1 = np.array([row1, row2, row3], dtype=np.float64)

    print("This is for matrix 2:")
    row1 = get_row(1)
    row2 = get_row(2)
    row3 = get_row(3)
    matrix2 = np.array([row1, row2, row3], dtype=np.float64)

    print("Here's matrix 1:")
    print(matrix1)

    print("Here's matrix 2:")
    print(matrix2)


    return matrix1, matrix2

def handle_phone():
    """
    Parameters: None

    Returns: None

    This function is the controller for obtaining and validating a
    phone number
    """
    phone_number = '-1'

    while not is_valid_phone(phone_number):
        phone_number = get_phone()

    print('Valid phone number. Thank you.')

def handle_zip4():
    """
    Parameters: None

    Returns: None

    This function is the controller for obtaining and validating a
    zip+4
    """
    zip4 = '-1'

    while not is_valid_zip4(zip4):
        zip4 = get_zip4()

    print('Valid ZIP+4. Thank you.')

def handle_matrix():
    """
    Parameters: None

    Returns: None

    This function does control over the matrix portion of the program.
    It calls the function that gets the matrices from the user. Then
    it displays a menu to the user to let the user determine what
    operation to perform on the matrices.
    """
    #help from here: https://stackoverflow.com/questions/2891790/
    # how-to-pretty-print-a-numpy-array-without-scientific-notation-and-with-given-pre
    #https://numpy.org/doc/stable/reference/generated/
    # numpy.set_printoptions.html#numpy.set_printoptions
    np.set_printoptions(precision=2, floatmode='fixed')


    matrix1, matrix2 = get_matrices()
    #test data
    # matrix1 = np.array([[1, 2, 4],
    #                     [4, 2, 1],
    #                     [3, 8, 9]])

    # matrix2 = np.array([[3, 2, 1],
    #                     [7, 2, 5],
    #                     [5, 2, 1]])

    choice = None

    while choice != 4:
        print("***Okay, let's have some fun with those matrices!***")
        print("1. Add")
        print("2. Subtract")
        print("3. Matrix multiplication")
        print("4. Element by element multiplication")
        print("5. Exit")
        choice = input("Please enter a number (1-5): ")

        if choice == "1":
            matrix3 = matrix1 + matrix2
            print(matrix1)
            print("+")
            print(matrix2)
            print("=")
            print(matrix3)
            print_trans_means(matrix3)
        elif choice == "2":
            matrix3 = matrix1 - matrix2
            print(matrix1)
            print("-")
            print(matrix2)
            print("=")
            print(matrix3)
            print_trans_means(matrix3)
        elif choice == "3":
            print("Matrix multiplication")
            matrix3 = np.matmul(matrix1, matrix2)
            print(matrix1)
            print("*")
            print(matrix2)
            print("=")
            print(matrix3)
            print_trans_means(matrix3)
        elif choice == "4":
            print("Matrix element multiplication")
            matrix3 = matrix1 * matrix2
            print(matrix1)
            print("*")
            print(matrix2)
            print("=")
            print(matrix3)
            print_trans_means(matrix3)
        elif choice == '5':
            print("Thank you for using this application")
            break

def is_valid_phone(number):
    """
    Parameters: A string

    Returns: True if the string is a regex match for a phone mumber per
    the constant REGEX_PHONE
    """
    return re.fullmatch(REGEX_PHONE, number)

def is_valid_zip4(zip4):
    """
    Parameters: A string

    Returns: True if the string is a regex match for zip+4 per the constant
    REGEX_ZIP4
    """
    return re.fullmatch(REGEX_ZIP4, zip4)

def main_menu():
    """
    Parameters: None

    Returns: None

    This function display the main menu and then call the appropriate
    routines based on the user unput
    """
    choice = None

    while choice != 4:
        print('***Welcome to Lab 4: Phones, ZIPs, and matrices***')
        print('1. Validate phone number')
        print('2. Validate ZIP+4')
        print('3. Matrix math')
        print('4. Exit')
        choice = input('Please enter a number (1-4): ')

        if choice == '1':
            handle_phone()
        elif choice == '2':
            handle_zip4()
        elif choice == '3':
            handle_matrix()
        elif choice == '4':
            print("Thank you for using this application")
            break

def main():
    """
    Parameters: None

    Returns: None

    This is just a stub that calls main_menu()
    """
    main_menu()

def print_trans_means(matrix):
    """
    Parameters: A 3x3 nparray

    Returns: None

    This function prints the transpose, row mean, and column mean of the
    matrxi that is based to it.
    """

    print("Transpose:")
    print(matrix.T)
    print("The mean of rows:")
    print(matrix.mean(axis=1))
    print("The mean of columns:")
    print(matrix.mean(axis=0))

main()

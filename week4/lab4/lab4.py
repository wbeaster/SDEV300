import re

import numpy as np
import pandas as pd

REGEX_PHONE = r"\d{3}-\d{3}-\d{4}"
REGEX_ZIP4 = r"\d{5}-\d{4}"

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

def get_row(num):
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

    #TODO: Clean up this language
    print("This is where the detailed instruction go (lenght, integer/float, etc")

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
    phone_number = '-1'

    while not is_valid_phone(phone_number):
        phone_number = get_phone()

    print('Valid phone number. Thank you.')

    return

def handle_zip4():
    zip4 = '-1'

    while not is_valid_zip4(zip4):
        zip4 = get_zip4()

    print('Valid ZIP+4. Thank you.')

    return

def handle_matrix():
    #matrix1, matrix2 = get_matrices()
    matrix1 = np.array([[1, 2, 4],
                        [4, 2, 1],
                        [3, 8, 9]])

    matrix2 = np.array([[3, 2, 1],
                        [7, 2, 5],
                        [5, 2, 1]])

    choice = None
    #TODO: Jsut added this, need to test it
    #help from here: https://stackoverflow.com/questions/2891790/how-to-pretty-print-a-numpy-array-without-scientific-notation-and-with-given-pre
    np.set_printoptions(precision=3)

    while choice != 4:
        print("***Okay, let's have some fun with those matrices!***")
        print("1. Add")
        print("2. Subtract")
        print("3. Matrix multiplication")
        print("4. Element by element multiplication")
        print("5. Exit")
        choice = input("Please enter a number (1-4): ")

        #TODO: Figure out he phraseology between matrix multiplication and element multiplication
        if choice == "1":
            matrix3 = matrix1 + matrix2
            print(matrix1)
            print("+")
            print(matrix2)
            print("=")
            print(matrix3)
            print("Transpose:")
            print(matrix3.T)
            #TODO: Round to the thousandths please
            print("The mean of rows:")
            print(matrix3.mean(axis=1))
            print("The mean of columns:")
            print(matrix3.mean(axis=0))
        elif choice == "2":
            matrix3 = matrix1 - matrix2
            print(matrix1)
            print("-")
            print(matrix2)
            print("=")
            print(matrix3)
        elif choice == "3":
            matrix3 = np.matmul(matrix1, matrix2)
            print(matrix1)
            print("*")
            print(matrix2)
            print("=")
            print(matrix3)
        elif choice == "4":
            matrix3 = matrix1 * matrix2
            print(matrix1)
            print("*")
            print(matrix2)
            print("=")
            print(matrix3)
        elif choice == '5':
            print("Thank you for using this application")
            break
    return
        
def is_valid_phone(number):
    return re.fullmatch(REGEX_PHONE, number)

def is_valid_zip4(zip4):
    return re.fullmatch(REGEX_ZIP4, zip4)

def main_menu():
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

    return

def main():
    main_menu()
    return

main()

"""
This is SDEV300 7384 Lab 5 - Python Data Analysis

This program will read csv fiels and then display Pandas generated
information from the contents of the file.
"""

import os

from matplotlib import pyplot as plt
import pandas as pd

LOC_POP_CHANGE = "/week5/lab5/PopChange.csv"
LOC_HOUSING = "/week5/lab5/Housing.csv"

def data_dump(data_frame, column):
    """
    Parameters:
    data_frame = Pandas data frame with the
    column = string of the column whose data will be displayed

    Returns: Nothing
    """
    pd.set_option('precision', 2)
    pd.set_option('display.float_format', '{:,.2f}'.format)
    #plt.ticklabel_format(style='plain')
    print(f"You selected {column}")
    print("The statistics for this column are:")
    print(data_frame[column].describe())
    plt.hist(data_frame[column], edgecolor='black')
    print("The histogram for this column is now displayed")
    plt.show()

def analyze_housing_data():
    """
    Parameters: None

    Returns: None

    This function displays a menu to the user, asks for their selection
    and then calls a function to display the appropriate data.
    """

    #open the file
    # pd.set_option('precision', 2)
    # pd.set_option('display.float_format', '{:,.2f}'.format)
    data_frame = pd.read_csv(os.getcwd() + LOC_HOUSING)

    #show a menu giving the user the choice on which column to analyze
    print("You selected housing data")

    choice = None

    while not choice:
        print("Select your choice:")
        print("1. Analyze 'AGE'")
        print("2. Analyze 'BEDRMS'")
        print("3. Analyze 'BUILT'")
        print("4. Analyze 'NUNITS'")
        print("5. Analyze 'ROOMS'")
        print("6. Analyze 'WEIGHT'")
        print("7. Analyze 'UTILITY'")
        print("8. Back")

        choice = input("Enter your choice (1 - 8): ")

        if choice == "1":
            data_dump(data_frame, "AGE")
            choice = None
        elif choice == "2":
            data_dump(data_frame, "BEDRMS")
            choice = None
        elif choice == "3":
            data_dump(data_frame, "BUILT")
            choice = None
        elif choice == "4":
            data_dump(data_frame, "NUNITS")
            choice = None
        elif choice == "5":
            data_dump(data_frame, "ROOMS")
            choice = None
        elif choice == "6":
            data_dump(data_frame, "WEIGHT")
            choice = None
        elif choice == "7":
            data_dump(data_frame, "UTILITY")
            choice = None
        elif choice == "8":
            break
        else:
            choice = None

def analyze_population_data():
    """
    Parameters: None

    Returns: None

    This function displays a menu to the user, asks for their selection
    and then calls a function to display the appropriate data.
    """

    pd.set_option('precision', 2)
    pd.set_option('display.float_format', '{:,.2f}'.format)
    data_frame = pd.read_csv(os.getcwd() + LOC_POP_CHANGE)
    data_frame.columns = ["id", "geography", "tgi", "tgi2", "pop_apr1", "pop_jul1", "delta"]

    print("You selected population data")

    choice = None

    while not choice:
        print("Select your choice:")
        print("1. Analyze 'pop_apr1'")
        print("2. Analyze 'pop_jul1'")
        print("3. Analyze 'delta' (change in population over time)")
        print("4. Back")

        choice = input("Enter your choice (1 - 4): ")

        if choice == "1":
            data_dump(data_frame, "pop_apr1")
            choice = None
        elif choice == "2":
            data_dump(data_frame, "pop_apr1")
            choice = None
        elif choice == "3":
            data_dump(data_frame, "delta")
            choice = None
        elif choice == "4":
            break
        else:
            choice = None

def main_menu():
    """
    Parameters: None

    Returns: None

    This function displays a menu to the user, asks for their selection
    and then calls a function to work a submenu.
    """

    choice = None

    while not choice:
        print("Select your choice:")
        print("1. Analyze population data")
        print("2. Analyze housing data")
        print("3. Exit")

        choice = input("Choice (1-3): ")

        if choice == "1":
            analyze_population_data()
            choice = None
        elif choice == "2":
            analyze_housing_data()
            choice = None
        elif choice == "3":
            break
        else:
            choice = None

main_menu()

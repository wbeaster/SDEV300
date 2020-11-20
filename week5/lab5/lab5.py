"""
This is SDEV300 7384 Lab 5 - Python Data Analysis

This program will read csv fiels and then display Pandas generated
information from the contents of the file.
"""

import os

from matplotlib import pyplot as plt
import pandas as pd

# TODO: use the data without Puerto Rico?
LOC_POP_CHANGE = "/week5/lab5/PopChange2.csv"
LOC_HOUSING = "/week5/lab5/Housing.csv"

def data_dump(df, column):
    """
    Parameters:
    df = Pandas data frame with the
    column = string of the column whose data will be displayed

    Returns: Nothing
    """
    print(f"You selected {column}")
    print("The statistics for this column are:")
    print(df[column].describe())
    plt.hist(df[column], edgecolor='black')
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
    pd.set_option('precision', 2)
    pd.set_option('display.float_format', '{:,.2f}'.format)
    df = pd.read_csv(os.getcwd() + LOC_HOUSING)

    #show a menu giving the user the choice on which column to analyze
    print("You selected population data")

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
        print("8. Exit")

        choice = input("Enter your choice (1 - 8): ")

        if choice == "1":
            data_dump(df, "AGE")
            choice = None
        elif choice == "2":
            data_dump(df, "BEDRMS")
            choice = None
        elif choice == "3":
            data_dump(df, "BUILT")
            choice = None
        elif choice == "4":
            data_dump(df, "NUNITS")
            choice = None
        elif choice == "5":
            data_dump(df, "ROOMS")
            choice = None
        elif choice == "6":
            data_dump(df, "WEIGHT")
            choice = None
        elif choice == "7":
            data_dump(df, "UTILITY")
            choice = None
        elif choice == "8":
            # TODO: I think we want to make it so just goes up a menu level
            break
        else:
            choice = None
    return

def analyze_population_data():
    """
    Parameters: None

    Returns: None

    This function displays a menu to the user, asks for their selection
    and then calls a function to display the appropriate data.
    """

    #TODO: Make it so it does not output exponential notation
    pd.set_option('precision', 2)
    pd.set_option('display.float_format', '{:,.2f}'.format)
    df = pd.read_csv(os.getcwd() + LOC_POP_CHANGE)
    df.columns = ["id", "geography", "tgi", "tgi2", "pop_apr1", "pop_jul1", "delta"]

    print("You selected population data")

    choice = None

    while not choice:
        print("Select your choice:")
        print("1. Analyze 'pop_apr1'")
        print("2. Analyze 'pop_jul1'")
        print("3. Analyze 'delta' (change in population over time)")
        print("4. Exit")

        choice = input("Enter your choice (1 - 4): ")

        if choice == "1":
            data_dump(df, "pop_apr1")
            choice = None
        elif choice == "2":
            data_dump(df, "pop_apr1")
            choice = None
        elif choice == "3":
            data_dump(df, "delta")
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
            break

main_menu()

import os

from matplotlib import pyplot as plt
import pandas as pd

LOC_POP_CHANGE = "/week5/lab5/PopChange.csv"
LOC_HOUSING = "/week5/lab5/Housing.csv"

def analyze_housing_data():
    #open the file
    #TODO: Make it so it does not output exponential notation
    pd.set_option('precision', 2)
    pd.set_option('display.float_format', '{:,.2f}'.format)
    df = pd.read_csv(os.getcwd() + LOC_HOUSING)
    #df.columns = ["id", "geography", "tgi", "tgi2", "pop_apr1", "pop_jul1", "delta"]
    print(df.columns)
    print(df.head())
    print(df.tail())
    
    #show a menu givning the user the choice on which column to analyze
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

        choice = input("Enter your choice (1 - 4): ")

        if choice == "1":
            #TODO: Print the describe of the data
            plt.hist(df["AGE"], edgecolor='black')
            plt.show()
            choice = None
        elif choice == "2":
            print(df.pop_jul1.describe())
            choice = None
        elif choice == "3":
            print(df.delta.describe())

            plt.hist(df["delta"])
            plt.show()

            choice = None
        elif choice == "8":
            # TODO: I think we want to make it so just goes up a menu level
            break
        else:
            choice = None
    
    #spit out the stats and the histogram
    #show the menu again
    return


def analyze_population_data():
    #open the file
    #TODO: Make it so it does not output exponential notation
    #TODO: Best video for 
    pd.set_option('precision', 2)
    pd.set_option('display.float_format', '{:,.2f}'.format)
    df = pd.read_csv(os.getcwd() + LOC_POP_CHANGE)
    df.columns = ["id", "geography", "tgi", "tgi2", "pop_apr1", "pop_jul1", "delta"]
    #print(df.columns)
    #print(df.head())
    #print(df.tail())
    
    #show a menu givning the user the choice on which column to analyze
    print("You selected population data")

    choice = None

    while not choice:
        print("Select your choice:")
        print("1. Analyze 'Pop Apr 1'")
        print("2. Analyze 'Pop Jul 1'")
        print("3. Analyze 'Change pop'")
        print("4. Exit")

        choice = input("Enter your choice (1 - 4): ")

        if choice == "1":
            #TODO: Print the describe of the data
            pops = df["pop_apr1"]
            #plt.hist(pops)
            # plt.hist(df["pop_apr1"], bins=5)
            plt.hist(df["pop_apr1"], log=True)
            plt.show()



            #df.hist(column="pop_apr1")
            #df.pop_apr1.hist()
            #plt.hist(df.pop_apr1)
            #plt.show()
            #histogram = df.pop_apr1.hist()
            #histogram = df.hist()
            #histogram.show()
            #df.hist().show()
            choice = None
        elif choice == "2":
            print(df.pop_jul1.describe())
            choice = None
        elif choice == "3":
            print(df.delta.describe())

            plt.hist(df["delta"])
            plt.show()

            choice = None
        elif choice == "4":
            break
        else:
            choice = None
    
    #spit out the stats and the histogram
    #show the menu again

def main_menu():
    choice = None
    
    while not choice:
        print("Select your choice:")
        print("1. Analyze population data")
        print("2. Analyze housing data")
        print("3. Exit")

        choice = input("Choice (1-3): ")

        if choice == "1":
            analyze_population_data()
        elif choice == "2":
            analyze_housing_data()
        elif choice == "3":
            break
        else:
            break
main_menu()
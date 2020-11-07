import os
import sys

import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image


RES_LOC = '/week3/lab3/res/'
"""
will be a list of dictionaries
Need to:
    Sort by state
    Search for a state and display selected traits
    Bar graph of top five states by population
    Update population

List of dictionaries
"""

states_list = [
    {
        'p_abb': 'AL',
        'name':'Alabama',
        'capital': 'Montgomery',
        'population': 1,
        'flower_name': 'Camelia',
        'flower_file': 'camellia-flower.jpg'
    },
    {
        'p_abb': 'AK',
        'name':'Alaska',
        'capital': 'Juneau',
        'population': 2,
        'flower_name': 'Forget Me Not'
    },
    {
        'p_abb': 'AZ',
        'name': 'Arizona',
        'capital': 'Phoenix',
        'population': 0,
        'flower_name': 'Saguaro Cactus Blossom'
    },
    {
        'p_abb': 'WY',
        'name': 'Wyoming',
        'capital': 'Cheyenne',
        'population': 3,
        'flower_name': 'Indian Paintbrush'
    },
    {
        'p_abb': 'AR',
        'name': 'Arkansas',
        'capital': 'Little Rock',
        'population': 67,
        'flower_name': 'Apple Blossom'
    }
]

def print_all_state_data_header():
    """
    Parameters: None
    Returns: None
    This function just prints the table header for state tables
    """

    print(f'{"State":<15}{"Capital":<15}{"Population":<15}{"Flower":<15}')

def print_all_state_data(abb):
    """
    Parameter: string: The state's two-letter postal abbreviation
    Returns: Nothing
    This function prints out a states data
    """
    result = list(filter(lambda s_list: s_list['p_abb'] == abb, states_list))

    print(f"{result[0]['name']:<15}", end="")
    print(f"{result[0]['capital']:<15}", end="")
    print(f"{result[0]['population']:<15}", end="")
    print(f"{result[0]['flower_name']}")

def display_flower(abb):
    """

    """
    #TODO: Write get_state which wraps this
    result = list(filter(lambda s_list: s_list['p_abb'] == abb, states_list))

    #It took me far longer than I wanted to figure out how to make the
    #path work properly. Ugh.
    #currentDirectory = os.getcwd()
    #dir = currentDirectory + '/week3/lab3/res/'
    #print(currentDirectory)
    #print(dir)
    #image = Image.open(dir + result[0]['flower_file'])
    image = Image.open(os.getcwd() + RES_LOC + result[0]['flower_file'])
    image.show()

def main_menu():
    """
    Parameters: None
    Returns: str of menu choice
    This function asks the user for their choice and the returns it
    """
    print('***Welcome to Lab3, fun with states!***')
    print('1. Display states in alphabetical order with additional information')
    print('2. Search by state and display additional information')
    print('3. Bar graph of top 5 states by population')
    print('4. Update a states population')
    print('5. Exit')

    return input('Choice (1-5): ')

def display_all_alpha():
    """
    Parameters: None
    Returns: None
    This function displays an alphabatized list of states and their
    corresponding additional data
    """

    sorted_states_list = sorted(states_list, key=lambda s: s['name'])
    
    print_all_state_data_header()
    for index in range(len(sorted_states_list)):
        print_all_state_data(sorted_states_list[index]['p_abb'])

def get_state():
    """
    Parameters: None
    Returns: String with state's two-letter postal abbreviation
    Asks and validates the user's state choice
    TODO: Tab completion?
    """

    state_choice = None

    #TODO: Make the code to handle bad user input

    state_choice = input("Enter the state (two-letter code or name: ").upper()

    return state_choice

def display_state(state_choice):
    """
    Parameters: the two-letter postal abbreviation of the selected state
    Returns: None
    This function display the state and data based on the state passed
    to it
    """

    print_all_state_data_header()
    print_all_state_data(state_choice)
    display_flower(state_choice)

def graph_top_five_pop():
    """
    Parameters: None
    Returns: None
    Displays a graph of the top five states by population
    TODO: Make sure test data changes population and then graphs top five population again
    """

    sorted_states_list = sorted(states_list, key=lambda p: p['population'], reverse=True)
    
    state_names = []
    state_pops = []
    
    for index in range(0, 5):
        state_names.append(sorted_states_list[index]['name'])
        state_pops.append(sorted_states_list[index]['population'])

    #state_pops = list_comprehension

    title = 'Five most populace states'
    sns.set_style('whitegrid')
    axes = sns.barplot(x=state_names, y=state_pops, palette='bright')
    axes.set_title(title)
    axes.set(xlabel='State', ylabel='Population')
    plt.show()

def get_updated_state_pop():
    """
    Paramters: None

    Returns: A tuple with state to be updated and the updated population
    """
    update_state = get_state()
    
    update_pop = None

    #TODO: Make it so this handles bad user input
    update_pop = input("Enter the new population (must be a positive integer): ")

    return update_state, update_pop
    

def update_state_pop(p_abb, updated_pop):
    """
    Paramters: 
    The two letter postal abbreviation for hte state to update
    The updated population for the state

    Returns: Nothing

    This function updates a state's population per the paramenters provided.
    Assumes that the postal abbreviation is valid. Assumes the population is
    a positive integer.
    """

    for index in range(0, len(states_list)):
        if states_list[index]['p_abb'] == p_abb:
            states_list[index]['population'] = int(updated_pop)

def main():

    choice = None

    while choice != '5':
        choice = main_menu()

        if choice == '1':
            display_all_alpha()
        elif choice == '2':
            state = get_state()
            display_state(state)
        elif choice == '3':
            graph_top_five_pop()
        elif choice == '4':
            name, updated_pop = get_updated_state_pop()
            update_state_pop(name, updated_pop)
        elif choice == '5':
            print("Thank you for using this application")

main()



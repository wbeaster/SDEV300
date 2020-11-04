"""
will be a dictionary of dictionaries
Need to:
    Sort by state
    Search for a state and display selected traits
    Bar graph of top five states by population
    Update population

Dictionary of dictionaries
"""

states = {
    'AL':
        {'name':'Alabama',
         'capital': 'Montgomery',
         'population': 2,
         'flower': 'alabama flower'},
    'AK':
        {'name':'Alaska',
        'capital': 'Juneau',
        'population': 1,
        'flower': 'alaska flower'}
}
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

    return input('Choice (1-5): ' )

def display_all_alpha():
    """
    Parameters: None
    Returns: None
    This function displays an alphabatized list of states and their
    corresponding additional data
    """

    #TODO: Make an alphabetized list/dictionary first

    print(f'{"State"} \t\t {"Capital"} \t\t {"Population"} \t\t {"Flower"}')
    for state_id in states:
        print(states[state_id]['name'], end="\t")
        print(f"\t{states[state_id]['capital']}")

def get_state():
    """
    Parameters: None
    Returns: String with state's name
    Asks and validates the user's state choice
    TODO: Tab completion?
    """

    return 'Alsaka' 

def display_state(state):
    """
    Parameters: None
    Returns: None
    This function display the state and data based on the state passed
    to it
    """

def graph_top_five_pop():
    return True

def update_state_pop():
    return True




choice = None
exit = False

while choice != exit:
    choice = main_menu()

    if choice == '1':
        display_all_alpha()
    elif choice == '2':
        state = get_state()
        display_state(state)
    elif choice == '3':
        graph_top_five_pop()
    elif choice == '4':
        update_state_pop()
    elif choice == '5':
        exit = True
    else:
        print("Please enter a choice from the menu.")
    




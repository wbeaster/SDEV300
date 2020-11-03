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
    'Alabama':
        {'capital': 'H',
         'popoulation': 2,
         'flower': 'test'},
    'Alaska':
        {'capital': 'A',
        'population': 1,
        'flower': 'alaska test'}
}

def display_main_menu():
    """
    Parameters: None
    Returns: None
    This function only dispalys the main menu
    """
    print('***Welcome to Lab3, fun with states!***')
    print('1. Display states in alphabetical order with additional information')
    print('2. Search by state and display additional information')
    print('3. Bar graph of top 5 states by population')
    print('4. Update a states population')
    print('5. Exit')

def main_menu_choice():
    """
    Parameters: None
    Returns: str of menu choice
    This function asks the user for their choice and the returns it
    """

    return input('Choice (1-5):' )

def display_all_alpha():
    """
    Parameters: None
    Returns: None
    This function displays an alphabatized list of states and their
    corresponding additional data
    """

def get_state():
    """
    Parameters: None
    Returns: String with state's name
    Asks and validates the user's state choice
    TODO: Tab completion?
    """

def display_state(state):
    """
    Parameters: None
    Returns: None
    This function display the state and data based on the state passed
    to it
    """





choice = None
exit = False

while choice != exit:
    display_main_menu()
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
    




"""
will be a dictionary of dictionaries
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
        'flower': 'alabama flower'
    },
    {
        'p_abb': 'AK',
        'name':'Alaska',
        'capital': 'Juneau',
        'population': 2,
        'flower': 'alaska flower'
    },
    {
        'p_abb': 'AA',
        'name': 'AA Alpha Test',
        'capital': 'aa Alpha Test',
        'population': 0,
        'flower': 'aa Alpha Test'}
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
    print(f"{result[0]['flower']}")

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
    




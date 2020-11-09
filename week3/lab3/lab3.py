"""
This is the program for SDEV300 7384 Lab 3

1. Display all U.S. States in Alphabetical order along with the Capital, State Population,and Flower
2. Search for a specific state and display the appropriate Capital name, State Population,and an
image of the associated State Flower.
3. Provide a Bar graph of the top 5populated States showing their overall population.
4. Update theoverall state populationfor a specific state.
5. Exit the program
"""

import os

import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image

RES_LOC = '/week3/lab3/res/'

states_list = [
    {
        'p_abb': 'AL',
        'name':'Alabama',
        'capital': 'Montgomery',
        'population': 4887870,
        'flower_name': 'Camelia',
        'flower_file': 'camellia-flower.jpg'
    },
    {
        'p_abb': 'AK',
        'name':'Alaska',
        'capital': 'Juneau',
        'population': 737438,
        'flower_name': 'Forget Me Not',
        'flower_file': 'Alpineforgetmenot.jpg'
    },
    {
        'p_abb': 'AZ',
        'name': 'Arizona',
        'capital': 'Phoenix',
        'population': 7171650,
        'flower_name': 'Saguaro Cactus Blossom',
        'flower_file': 'saguaroflowersFlickr.jpg'
    },
    {
        'p_abb': 'WY',
        'name': 'Wyoming',
        'capital': 'Cheyenne',
        'population': 577737,
        'flower_name': 'Indian Paintbrush',
        'flower_file': ''
    },
    {
        'p_abb': 'AR',
        'name': 'Arkansas',
        'capital': 'Little Rock',
        'population': 3013820,
        'flower_name': 'Apple Blossom',
        'flower_file': 'AppletreeblossomArkansasflower.JPG'
    },
    {
        'p_abb': 'CA',
        'name': 'California',
        'capital': 'Sacramento',
        'population': 39557000,
        'flower_name': 'California Poppy',
        'flower_file': 'CAflowerCaliforniaPoppy.jpg'
    },
    {
        'p_abb': 'CO',
        'name': 'Colorado',
        'capital': 'Denver',
        'population': 5695560,
        'flower_name': 'White and Lavender Columbine',
        'flower_file': 'Colorado_columbine2.jpg'
    },
    {
        'p_abb': 'CT',
        'name': 'Connecticut',
        'capital': 'Hartford',
        'population': 3572660,
        'flower_name': 'Mountain Laurel',
        'flower_file': 'Mountain-Laural-flowers2.jpg'
    },
    {
        'p_abb': 'DE',
        'name': 'Delaware',
        'capital': 'Dover',
        'population': 967171,
        'flower_name': 'Peach Blossom',
        'flower_file': 'peachblossomspeachflowers.jpg'
    },
    {
        'p_abb': 'FL',
        'name': 'Florida',
        'capital': 'Tallahassee',
        'population': 21299300,
        'flower_name': 'Orange Blossom',
        'flower_file': 'OrangeBlossomsFloridaFlower.jpg'
    },
    {
        'p_abb': 'GA',
        'name': 'Georgia',
        'capital': 'Atlanta',
        'population': 10519500,
        'flower_name': 'Cherokee Rose',
        'flower_file': 'CherokeeRoseFlower.jpg'
    },
    {
        'p_abb': 'HI',
        'name': 'Hawaii',
        'capital': 'Honolulu',
        'population': 1420490,
        'flower_name': 'Yellow Hibiscus/Pua Aloalo',
        'flower_file': 'yellowhibiscusPuaAloalo.jpg'
    },
    {
        'p_abb': 'ID',
        'name': 'Idaho',
        'capital': 'Boise',
        'population': 1754210,
        'flower_name': 'Syringa',
        'flower_file': 'syringaPhiladelphuslewisiiflower.jpg'
    },
    {
        'p_abb': 'IL',
        'name': 'Illinois',
        'capital': 'Springfield',
        'population': 12741100,
        'flower_name': 'Purple Violet',
        'flower_file': 'violetsflowers.jpg'
    },
    {
        'p_abb': 'IN',
        'name': 'Indiana',
        'capital': 'Indianapolis',
        'population': 6691880,
        'flower_name': 'Peony',
        'flower_file': 'PeonyPaeoniaflowers.jpg'
    },
    {
        'p_abb': 'IA',
        'name': 'Iowa',
        'capital': 'Des Moines',
        'population': 3156140,
        'flower_name': 'Wild Prairie Rose',
        'flower_file': 'WildPrairieRose.jpg'
    },
    {
        'p_abb': 'KS',
        'name': 'Kansas',
        'capital': 'Topeka',
        'population': 2911500,
        'flower_name': 'Sunflower',
        'flower_file': 'native-sunflowers.jpg'
    },
    {
        'p_abb': 'KY',
        'name': 'Kentucky',
        'capital': 'Frankfort',
        'population': 4468400,
        'flower_name': 'Goldenrod',
        'flower_file': 'stateflowergoldenrod-bloom.jpg'
    },
    {
        'p_abb': 'LA',
        'name': 'Lousiana',
        'capital': 'Baton Rouge',
        'population': 4659980,
        'flower_name': 'Magnolia',
        'flower_file': 'MagnoliagrandifloraMagnoliaflower.jpg'
    },
    {
        'p_abb': 'ME',
        'name': 'Maine',
        'capital': 'Augusta',
        'population': 1338400,
        'flower_name': 'White Pine Cone and Tassel',
        'flower_file': 'whitepinemalecones.jpg'
    },
    {
        'p_abb': 'MD',
        'name': 'Maryland',
        'capital': 'Annapolis',
        'population': 6042720,
        'flower_name': 'Black-Eyed Susan',
        'flower_file': 'FlowerMDBlack-eyedSusan.jpg'
    },
    {
        'p_abb': 'MA',
        'name': 'Massachusetts',
        'capital': 'Boston',
        'population': 6902150,
        'flower_name': 'Mayflower',
        'flower_file': 'MayflowerTrailingArbutus.jpg'
    },
    {
        'p_abb': 'MI',
        'name': 'Michigan',
        'capital': 'Lansing',
        'population': 9995920,
        'flower_name': 'Apple Blossom',
        'flower_file': 'appleblossombeauty.jpg'
    },
    {
        'p_abb': 'MN',
        'name': 'Minnesota',
        'capital': 'Saint Paul',
        'population': 5611180,
        'flower_name': 'Pink and White Lady Slipper',
        'flower_file': 'pinkwhiteladysslipperflower1.jpg'
    },
    {
        'p_abb': 'MS',
        'name': 'Mississippi',
        'capital': 'Jackson',
        'population': 2986530,
        'flower_name': 'Magnolia',
        'flower_file': 'magnoliablossomflower01.jpg'
    },
    {
        'p_abb': 'MO',
        'name': 'Missouri',
        'capital': 'Jefferson City',
        'population': 6126450,
        'flower_name': 'White Hawthorn Blossom',
        'flower_file': 'hawthornflowersblossoms1.jpg'
    },
    {
        'p_abb': 'MT',
        'name': 'Montana',
        'capital': 'Helena',
        'population': 1062300,
        'flower_name': 'Bitterroot',
        'flower_file': 'bitterrootfloweremblem.jpg'
    },
    {
        'p_abb': 'NE',
        'name': 'Nebraska',
        'capital': 'Lincoln',
        'population': 1929270,
        'flower_name': 'Goldenrod',
        'flower_file': 'goldenrodflowersyellow4.jpg'
    },
    {
        'p_abb': 'NV',
        'name': 'Nevada',
        'capital': 'Carson City',
        'population': 3034390,
        'flower_name': 'Sagebrush',
        'flower_file': 'Nevada-Sagebrush-Artemisia-tridentata.jpg'
    },
    {
        'p_abb': 'NH',
        'name': 'New Hampshire',
        'capital': 'Concord',
        'population': 1356460,
        'flower_name': 'Purple Lilac',
        'flower_file': 'lilacflowerspurplelilac.jpg'
    },
    {
        'p_abb': 'NJ',
        'name': 'New Jersey',
        'capital': 'Trenton',
        'population': 8908520,
        'flower_name': 'Violet',
        'flower_file': 'wood-violet.jpg'
    },
    {
        'p_abb': 'NM',
        'name': 'New Mexico',
        'capital': 'Santa Fe',
        'population': 2095430,
        'flower_name': 'Yucca Flower',
        'flower_file': 'YuccaFlowersclose.jpg'
    },
    {
        'p_abb': 'NY',
        'name': 'New York',
        'capital': 'Albany',
        'population': 19542200,
        'flower_name': 'Rose',
        'flower_file': 'redrosebeautystateflowerNY.jpg'
    },
    {
        'p_abb': 'NC',
        'name': 'North Carolina',
        'capital': 'Raleigh',
        'population': 10383600,
        'flower_name': 'Dogwood',
        'flower_file': 'NCarolinaLilywildflower2.jpg'
    },
    {
        'p_abb': 'ND',
        'name': 'North Dakota',
        'capital': 'Bismarck',
        'population': 760077,
        'flower_name': 'Wild Prairie Rose',
        'flower_file': 'flowerwildprairierose.jpg'
    },
    {
        'p_abb': 'OH',
        'name': 'Ohio',
        'capital': 'Columbus',
        'population': 11689400,
        'flower_name': 'Scarlet Carnation',
        'flower_file': 'WhitetrilliumTrilliumgrandiflorum.jpg'
    },
    {
        'p_abb': 'OK',
        'name': 'Oklahoma',
        'capital': 'Oklahoma City',
        'population': 3943080,
        'flower_name': 'Mistletoe',
        'flower_file': 'mistletoe_phoradendron_serotinum.jpg'
    },
    {
        'p_abb': 'OR',
        'name': 'Oregon',
        'capital': 'Salem',
        'population': 4190710,
        'flower_name': 'Oregon Grape',
        'flower_file': 'Oregongrapeflowers2.jpg'
    },
    {
        'p_abb': 'PA',
        'name': 'Pennsylvania',
        'capital': 'Harrisburg',
        'population': 12807100,
        'flower_name': 'Mountain Laurel',
        'flower_file': 'Mt_Laurel_Kalmia_Latifolia.jpg'
    },
    {
        'p_abb': 'RI',
        'name': 'Rhode Island',
        'capital': 'Providence',
        'population': 1057320,
        'flower_name': 'Violet',
        'flower_file': 'violetsflowers.jpg'
    },
    {
        'p_abb': 'SC',
        'name': 'South Carolina',
        'capital': 'Columbia',
        'population': 5084130,
        'flower_name': 'Yellow Jessamine',
        'flower_file': 'CarolinaYellowJessamine101.jpg'
    },
    {
        'p_abb': 'SD',
        'name': 'South Dakota',
        'capital': 'Pierre',
        'population': 882235,
        'flower_name': 'Pasque Flower',
        'flower_file': 'Pasqueflower-03.jpg'
    },
    {
        'p_abb': 'TN',
        'name': 'Tennessee',
        'capital': 'Nashville',
        'population': 6770010,
        'flower_name': 'Iris',
        'flower_file': 'purpleirisflower.jpg'
    },
    {
        'p_abb': 'TX',
        'name': 'Texas',
        'capital': 'Austin',
        'population': 28701800,
        'flower_name': 'Bluebonnet',
        'flower_file': 'BluebonnetsBlueRed.jpg'
    },
    {
        'p_abb': 'UT',
        'name': 'Utah',
        'capital': 'Salt Lake City',
        'population': 3161100,
        'flower_name': 'Sego Lily',
        'flower_file': 'SegoLily.jpg'
    },
    {
        'p_abb': 'VT',
        'name': 'Vermont',
        'capital': 'Montpelier',
        'population': 626299,
        'flower_name': 'Red Clover',
        'flower_file': 'redcloverstateflowerWV.jpg'
    },
    {
        'p_abb': 'VA',
        'name': 'Virginia',
        'capital': 'Richmond',
        'population': 8517680,
        'flower_name': 'Dogwood',
        'flower_file': 'floweringDogwoodSpring.jpg'
    },
    {
        'p_abb': 'WA',
        'name': 'Washington',
        'capital': 'Olympia',
        'population': 7535590,
        'flower_name': 'Pink Rhododendron',
        'flower_file': 'flower_rhododendronWeb.jpg'
    },
    {
        'p_abb': 'WV',
        'name': 'West Virginia',
        'capital': 'Charleston',
        'population': 1805830,
        'flower_name': 'Rhododendron',
        'flower_file': 'rhododendronWVstateflower.jpg'
    },
    {
        'p_abb': 'WI',
        'name': 'Wisconsin',
        'capital': 'Madison',
        'population': 5813570,
        'flower_name': 'Wood Violet',
        'flower_file': 'wood-violet.jpg'
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
    print(f"{result[0]['population']:<15,}", end="")
    print(f"{result[0]['flower_name']}")

def display_flower(abb):
    """
    Paramters: The postal abbreviation for the state who's flower should
    be displayed. Assumes a valid postal abbreviation

    Returns: None


    """
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
    for state in sorted_states_list:
        print_all_state_data(state['p_abb'])

def get_state():
    """
    Parameters: None

    Returns: String with state's two-letter postal abbreviation.

    Asks and validates the user's state choice
    """

    choice = None

    while choice is None:
        choice = input("Enter the state (two-letter code or name: ").upper()
        if len(choice) == 2:
            result = list(filter(lambda s_list: s_list['p_abb'] == choice, states_list))
        else:
            result = list(filter(lambda s_list: s_list['name'].upper() == choice, states_list))
        if len(result) == 0:
            print(f"{choice} is not a valid choice.")
            choice = None

    return result[0]['p_abb']

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
    axes.set_ylim(top=state_pops[0] * 1.1)
    axes.set_ylim([0, 40000000])
    plt.show()

def get_updated_pop():
    """
    Paramters: None

    Returns: A positive integer containing the value to be the new state
    population
    """
    updated_pop = None

    while not updated_pop:
        updated_pop = input("Enter the new population (must be an integer 0 or greater): ")
        if not updated_pop.isnumeric():
            updated_pop = None
        elif int(updated_pop) < 0:
            updated_pop = None

    return int(updated_pop)

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

#    for index in range(0, len(states_list)):
#        if states_list[index]['p_abb'] == p_abb:
#            states_list[index]['population'] = int(updated_pop)

    for state in states_list:
        if state['p_abb'] == p_abb:
            state['population'] = int(updated_pop)


def main():
    """
    This is the main function for the program. The main loop runs in it
    and some variables that the linter might think are constants are here
    """

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
            name = get_state()
            updated_pop = get_updated_pop()
            update_state_pop(name, updated_pop)
        elif choice == '5':
            print("Thank you for using this application")

main()

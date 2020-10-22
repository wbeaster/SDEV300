


#according to wikipedia, this is the age of the oldest living Ameircan
#I add one year because 115.1 is > 115 but is still valid.
OLDEST_AGE = 116
STATE_CODES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", 
    "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", 
    "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD",
    "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
GREATEST_ZIP = "99950"
LEAST_ZIP = "000501"

def queryContinue():
    """
    DRY for asking whether the user wants to continue
    Since we ask after every question, this should be a function
    """
    print("Continue? (y/n): ")
    proceed = input()
    
    if (proceed != 'y'):
        exit(0)

def main():
    """
    Talk about it here
    """

    #initialize variables here
    firstName = ""
    lastName = ""
    age = -1
    citizen = ""
    state = ""
    zipcode = -1

    #body
    print("Welcome to the Python Voter Registration Application.")
    queryContinue()

    firstName = input("First name: ")
    queryContinue()

    lastName = input("Last name: ")
    queryContinue()

    # and not isinstance(age, int)):
    while (age < 0 or age > OLDEST_AGE):
        print(f"Age (18 - {OLDEST_AGE}):", end=" ")
        age = int(input())
    if (age < 18):
        print("You are too young to vote. Exiting program.")
        exit(0)
    queryContinue()

    citizen = input("Are you a US citizen (y/n): ")
    if (citizen != 'y'):
        exit(0)
    #TODO: make a variable yes = ['y', 'Y', 'yes', 'YES"] and test for
    #in that set to continue
    queryContinue()

    while (not (state in STATE_CODES)):
        state = input("Type the two letter code for you state of residence: ")
    queryContinue()

    while(not (int(LEAST_ZIP) < int(zipcode) < int(GREATEST_ZIP))):
        zipcode = input("Zipcode: ")

    print("Thank you for registering to vote. Here is the information",
        "received:")
    print(f"Name: {firstName} {lastName}")
    print(f"Age: {age}")
    print(f"U.S. citizen: {citizen}")
    print(f"State:  {state}")
    print(f"Zipcode:  {zipcode}")
    print("Thanks for trying theVoter Registration Application. Your voter",
        "registration card should be shipped within 3 weeks.")

main()



    

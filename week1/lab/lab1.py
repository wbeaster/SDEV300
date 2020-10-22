


#according to wikipedia, this is the age of the oldest living Ameircan
OLDEST_AGE = 115
STATE_CODES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", 
    "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", 
    "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD",
    "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
GREATEST_ZIP = "99950"
LEAST_ZIP = "000501"

def queryContinue():
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
        print(f"Age (0 - {OLDEST_AGE}):", end=" ")
        age = int(input())
    queryContinue()

    citizen = input("Are you a US citizen (y/n): ")
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



    

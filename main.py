# have to import hella functionaliy up here
# Connection should be made each time you run a command?
# Make sure that its ACID property stays

# python -m pip install XXX

import tableprint as tp
import functions
import time

def main():


    print("Welcome to The Bank of Stories! ")
    time.sleep(1)
    print("We are a privately owned company by our lord and savior... ")
    time.sleep(2)
    print(".........................................................")
    print("........................................................")
    print(".......................................................")
    print("......................................................")
    print(".....................................................")
    print("....................................................")
    print("...................................................")
    print("..................................................")
    print(".................................................")
    print("................................................")
    print("...............................................")
    print("..............................................")
    print(".............................................")
    print("............................................")
    print("...........................................")
    print("..........................................")
    print(".........................................")
    print("........................................")
    print(".......................................")
    print("......................................")
    print(".....................................")
    print("....................................")
    print("...................................")
    print("..................................")
    print(".................................")
    print("................................")
    print("...............................")
    print("..............................")
    print(".............................")
    print("............................")
    print("...........................")
    print("..........................")
    print(".........................")
    print("........................")
    print(".......................")
    print("......................")
    print(".....................")
    print("....................")
    print("...................")
    print("...Charlie Story... ")
    time.sleep(2)
    print("1. Sign Up A New Customer ")
    print("0. Quit")
    try:
        choice = int(input())
    except:
        print("Invalid Choice")
        choice = 0
    if choice == 0:
        tp.banner("Exiting Prematurely")
    else:
        listofcon = functions.Create_Connection()
        functions.Create_New_Customer(listofcon);

    while choice != 0:
        signed_in = 0
        print("--- Main Menu --- ")
        print("1. Create Account (Know customer ID) ")  # what is the diff exactly?
        print("2. Sign In (Know account Num) ")
        print("3. Add/Withdrawl From Balance ")
        print("4. Transfer Cash Between Accounts ")
        print("5. View Customers")
        if signed_in == 1:
            print("6. View All Data")
        print("0. Quit ")

        try:
            choice = int(input())
        except:
            print("Invalid Choice")
            choice = 420
            continue

        if choice == 1:
            functions.Create_Account(listofcon);

        elif choice == 2:
            functions.sign_in(listofcon);
            signed_in = 1
        elif choice == 3:
            functions.add_withdrawl_transfer_balance(listofcon,2);

        elif choice == 4:
            functions.add_withdrawl_transfer_balance(listofcon,1);

        elif choice == 5:
            functions.view_Customers(listofcon);

        elif choice == 6:
            functions.view_all_data(listofcon);

        elif choice == 0:
            tp.banner("Exiting Banking Application") # if yours doesn' run change any tp to print
        else:
            print("Error: invalid choice received. Please re-enter an integer ")


if __name__ == "__main__":
	main()

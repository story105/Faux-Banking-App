# have to import hella functionaliy up here
# Connection should be made each time you run a command?
# Make sure that its ACID property stays

# python -m pip install XXX

import tableprint as tp
import functions

def main():


    print("--- Entry Menu --- ")
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
        functions.Create_New_Customer();
    while choice != 0:

        print("--- Main Menu --- ")
        print("1. Create Account (Know customer ID) ")  # what is the diff exactly?
        print("2. Sign In (Know account Num) ")
        print("3. Add/Withdrawl From Balance ")
        print("4. Transfer Cash Between Accounts ")
        print("0. Quit ")

        try:
            choice = int(input())
        except:
            print("Invalid Choice")
            choice = 420
            continue

        if choice == 1:
            functions.Create_Account();

        elif choice == 2:
            functions.sign_in();

        elif choice == 3:
            functions.add_withdrawl_balance();

        elif choice == 4:
            functions.transfer_money();

        elif choice == 0:
            tp.banner("Exiting Banking Application") # if yours doesn' run change any tp to print
        else:
            print("Error: invalid choice received. Please re-enter an integer ")


if __name__ == "__main__":
	main()

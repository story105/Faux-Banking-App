# have to import hella functionaliy up here
# Connection should be made each time you run a command?
# Make sure that its ACID property stays
import tableprint as tp
import functions

def main():

    choice = 1

    while choice != 0:

        print("--- Main Menu --- ")
        print("1. Sign Up A New Customer ")
        print("2. Create Account ")  # what is the diff exactly?
        print("3. Sign In ")
        print("4. CHARLIE MAKE MORE FUNCT? ")
        print("0. Quit ")

        try:
            choice = int(input())
        except:
            print("Invalid Choice")
            choice = 420
            continue

        if choice == 1:
            functions.Create_New_Customer();

        elif choice == 2:
            functions.Create_Account();

        elif choice == 3:
            functions.sign_in();

        elif choice == 0:
            tp.banner("Exiting Banking Application") # if yours doesn' run change any tp to print
        else:
            print("Error: invalid choice received. Please re-enter an integer ")


if __name__ == "__main__":
	main()

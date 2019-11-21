import pymysql
import sqlite3
import pandas as pd
from random import randint
import time, datetime
from decimal import Decimal

# ------------------------------------
# MySQL
# ------------------------------------
def create_mysql_connection(db_user, db_password, host_name, db_name):
    conn = None
    try:
        conn = pymysql.connect(user=db_user, password=db_password, host=host_name, db=db_name)
    except:
        print('connection failed')
    return conn

# create MySQL connection and cursor
def Create_Connection():
    mysql_conn = create_mysql_connection(db_user='root', db_password='', host_name='104.198.197.253', db_name='Bank')
    mysql_cur = mysql_conn.cursor()
    return([mysql_cur,mysql_conn])

def get_Curr_Time():
    ts_epoch = time.time()
    ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
    return(ts)
    # '2013-03-03 01:03:02' format

#insert_sql = '''INSERT INTO goods(item_id, flavor, food, price)
#                         VALUES (?,?,?,?)'''
#insert_vals = ('1', 'Strawberry', 'Ice Cream', 10.50)
#sqlite_cur.execute(insert_sql, insert_vals)

    # UPDATE statement
#update_sql = '''UPDATE goods
#                   SET flavor = ?
#                 WHERE item_id = ?
#             '''
#update_vals = ('Vanilla', '1')
#sqlite_cur.execute(update_sql, update_vals)

#Printing stuff
#mysql_cur.execute('SELECT * FROM Customer;')
#result = mysql_cur.fetchall()
#for row in result:
#    print(row)

# Load DB to pandas for analysis
#mysql_pandas = pd.read_sql('SELECT * FROM Customer;', con=mysql_conn)
#print(mysql_pandas.head())


def Create_New_Customer(ListOfCons):
    mysql_cur = ListOfCons[0]
    mysql_conn = ListOfCons[1]

    print("Please enter an SSN: ")
    try:
        SSN = int(input())
    except:
        print("Invalid Input. Providing random SSN ")
        SSN = randint(100000000, 999999999)

    print("Please enter a first name: ")
    FN = input()
    print("Please enter a last name: ")
    LN = input()
    customer_ID = randint(10,9999) # low chance of overlap

    insert_sql = '''INSERT INTO Customer(customer_id, SSN, first_name, last_name)
                             VALUES (%s,%s,%s,%s);'''
    insert_vals = (customer_ID, SSN, FN, LN)
    print(insert_vals)
    print("")
    mysql_cur.execute(insert_sql, insert_vals)

    customer_ID = str(customer_ID)
    mysql_pandas = pd.read_sql('SELECT * FROM Customer WHERE customer_id = ' + customer_ID + ";", con=mysql_conn)
    print(mysql_pandas.head())

    print("Please review your information above. ")
    print("")

def Create_Account(ListOfCons):

    mysql_cur = ListOfCons[0]
    mysql_conn = ListOfCons[1]
    print("Enter your customer ID")
    try:
        customer_ID = int(input())
    except:
        print("Invalid Input. Please enter a valid Customer ID ")

    print("")
    print("Please select which type of account you'd like!")
    print("1: Checkings")
    print("2: Savings")
    try:
        account_type = int(input())
    except:
        print("Invalid Input. Creating 'Checking' account ")
        account_type = 1
    if account_type == 1:
        account_type = "Checkings"
    elif account_type == 2:
        account_type = "Savings"
    else:
        account_type = "Checkings"

    print("Do you wish to add money to your account (type 'yes' or 'no')? ")
    inputted = input()
    if inputted.lower() == "no":
        input_cash = 0
    elif (inputted.lower() == "yes"):
        print("How much do you wish to add? ")
        try:
            input_cash = Decimal(input())
        except:
            print("Invalid Input. Adding base amount $420 ")
            input_cash = 420
    else:
        print("Couldn't decipher your request. Transferring $69 pity dollars to your {0} account.".format(account_type))
        input_cash = 69


    account_num = randint(0, 99999999)

    insert_sql = '''INSERT INTO Account_xref(customer_id, account_num)
                             VALUES (%s,%s)'''
    insert_vals = (customer_ID, account_num) # input cash == balance
    mysql_cur.execute(insert_sql, insert_vals)

    insert_sql = '''INSERT INTO Account(account_num, account_type, balance)
                             VALUES (%s,%s,%s)'''
    insert_vals = (account_num, account_type, input_cash) # input cash == balance
    mysql_cur.execute(insert_sql, insert_vals)

    # INPUT INTO TRANSACTION_LOG fuck
    if input_cash > 0:
        insert_sql = '''INSERT INTO Transaction_log(timestamp, trans_id, account_num, trans_type, trans_amount)
                            VALUES (%s,%s,%s,%s,%s)'''
        timestamp1 = get_Curr_Time()
        trans_id = randint(1,999999)
        trans_type = "Addition"
        insert_vals = (timestamp1, trans_id, account_num, trans_type, input_cash) # input cash == balance
        mysql_cur.execute(insert_sql, insert_vals)

    account_num = str(account_num)
    mysql_pandas = pd.read_sql('SELECT * FROM Account WHERE account_num = ' + account_num + ";", con=mysql_conn)
    print(mysql_pandas.head())

    print("Please review Account information above. ")
    print("")

def sign_in(ListOfCons):
    mysql_cur = ListOfCons[0]
    mysql_conn = ListOfCons[1]
    print("Please enter the number which account you'd like to access?")
    try:
        account_num = int(input())
    except:
        print("Invalid Input. ")

    account_num = str(account_num)
    print("Please purview your data: ")
    mysql_pandas = pd.read_sql('SELECT * FROM Account WHERE account_num = ' + account_num + ";", con=mysql_conn)
    print(mysql_pandas.head())
    print("Customer ID: ")
    mysql_pandas = pd.read_sql('SELECT customer_id FROM Account_xref WHERE account_num = ' + account_num + ";", con=mysql_conn)
    print(mysql_pandas.head())
    print("If you have done any transferring of money: ")
    mysql_pandas = pd.read_sql('SELECT * FROM Transaction_log WHERE account_num = ' + account_num + ";", con=mysql_conn)
    print(mysql_pandas.head())
    print("")

def view_all_data(ListOfCons):
    mysql_cur = ListOfCons[0]
    mysql_conn = ListOfCons[1]
    mysql_pandas = pd.read_sql('SELECT * FROM Customer', con=mysql_conn)
    print(mysql_pandas.head())
    time.sleep(2)
    mysql_pandas = pd.read_sql('SELECT * FROM Account', con=mysql_conn)
    print(mysql_pandas.head())
    time.sleep(2)
    mysql_pandas = pd.read_sql('SELECT * FROM Account_xref', con=mysql_conn)
    print(mysql_pandas.head())
    time.sleep(2)
    mysql_pandas = pd.read_sql('SELECT * FROM Transaction_log', con=mysql_conn)
    print(mysql_pandas.head())
    time.sleep(2)
    print("Be responsible")


def add_withdrawl_transfer_balance(ListOfCons,selection):
    mysql_cur = ListOfCons[0]
    mysql_conn = ListOfCons[1]

    mysql_pandas = pd.read_sql('SELECT * FROM Account', con=mysql_conn)
    print(mysql_pandas.head())
    print("Enter your account number")
    try:
        account_num = int(input())
    except:
        print("Invalid Input. Please enter a valid Account Num ")

    print("Do you wish to add money to your account (type 'yes' or 'no')? ")
    choice = input()
    choice_inp = 4 # nothing
    if choice.lower() == "no":
        print("Do you wish to Withdrawl (type 'yes' or 'no')? ")
        choice2 = input()

        if choice2.lower() == "no":
            print("You really went through all this to not do anything???")
            print("You gonna wait in timeout")
            time.sleep(10)
            choice_inp = 4 # nothing

        # withdraw
        elif choice2.lower() == "yes":
            choice_inp = 2
            print("How much do you wish to take out? ")
            try:
                withdraw_cash = Decimal(input())
            except:
                print("Invalid number.")
                withdraw_cash = 0
                # Withdrawl done
        else:
            print(".......... bruh")
    # for adding
    elif (choice.lower() == "yes"):
        choice_inp = 1
        print("How much do you wish to add? ")
        try:
            input_cash = Decimal(input())
        except:
            print("Invalid Input.")
            input_cash = 0
    else:
        print("Couldn't decipher your request. Adding $69 pity dollars to your #{0} account.".format(account_num))
        input_cash = 69

    trans_id = randint(100,99999999)

    if selection == 1:
        print("Do you wish to transfer funds (type 'yes' or 'no')? ")
        choice3 = input()
        if choice3.lower() == "no":
            print("Why you like this?")
        elif choice3.lower() == "yes":
            choice_inp = 3 # transfer
            print("How much do you want to transfer?")
            try:
                trans_cash = Decimal(input())
            except:
                print("Invalid Input.")
                trans_cash = 0
            print("To which account?")
            try:
                account_num2 = int(input())
            except:
                print("Invalid Input.")
                account_num2 = 0
        else:
            print("Bruhhh again?")
    if choice_inp == 1: # change these to update
        mysql_cur.execute('SELECT balance FROM Account WHERE account_num = ' + account_num  + ';')
        result = mysql_cur.fetchall()
        print(result)
        update_sql = '''UPDATE Account
                        SET balance = ?
                        WHERE account_num = ?
                     '''
        update_vals = (input_cash, account_num)
        mysql_cur.execute(update_sql, update_vals)

        insert_sql = '''INSERT INTO Transaction_log(timestamp, trans_id, account_num, trans_type, trans_amount)
                            VALUES (%s,%s,%s,%s,%s)'''
        timestamp1 = get_Curr_Time()
        trans_id = randint(1,999999)
        trans_type = "Addition"
        insert_vals = (timestamp1, trans_id, account_num, trans_type, input_cash) # input cash == balance
        mysql_cur.execute(insert_sql, insert_vals)

        mysql_pandas = pd.read_sql('SELECT * FROM Transaction_log WHERE account_num = ' + account_num + ";", con=mysql_conn)
        print(mysql_pandas.head())

    elif choice_inp == 2:
        update_sql = '''UPDATE Account
                        SET balance = ?
                        WHERE account_num = ?
                     '''
        update_vals = (withdraw_cash, account_num)
        mysql_cur.execute(update_sql, update_vals)

        insert_sql = '''INSERT INTO Transaction_log(timestamp, trans_id, account_num, trans_type, trans_amount)
                            VALUES (%s,%s,%s,%s,%s)'''
        timestamp1 = get_Curr_Time()
        trans_id = randint(1,999999)
        trans_type = "Subtraction"
        insert_vals = (timestamp1, trans_id, account_num, trans_type, input_cash) # input cash == balance
        mysql_cur.execute(insert_sql, insert_vals)

        mysql_pandas = pd.read_sql('SELECT * FROM Transaction_log WHERE account_num = ' + account_num + ";", con=mysql_conn)
        print(mysql_pandas.head())

    elif choice_inp == 3: # transfer
        update_sql = '''UPDATE Account
                        SET balance = ?
                        WHERE account_num = ?
                     '''
        update_vals = (trans_cash, account_num)
        mysql_cur.execute(update_sql, update_vals)
        update_sql = '''UPDATE Account
                        SET balance = ?
                        WHERE account_num = ?
                     '''
        update_vals = (trans_cash, account_num2)
        mysql_cur.execute(update_sql, update_vals)


        insert_sql = '''INSERT INTO Transaction_log(timestamp, trans_id, account_num, trans_type, trans_amount)
                            VALUES (%s,%s,%s,%s,%s)'''
        timestamp1 = get_Curr_Time()
        trans_id = randint(1,999999)
        trans_type = "Subtraction"
        insert_vals = (timestamp1, trans_id, account_num, trans_type, trans_cash) # input cash == balance
        mysql_cur.execute(insert_sql, insert_vals)
        insert_sql = '''INSERT INTO Transaction_log(timestamp, trans_id, account_num, trans_type, trans_amount)
                            VALUES (%s,%s,%s,%s,%s)'''
        timestamp2 = get_Curr_Time()
        trans_id2 = randint(1,999999)
        trans_type = "Addition"
        insert_vals = (timestamp2, trans_id2, account_num2, trans_type, trans_cash) # input cash == balance
        mysql_cur.execute(insert_sql, insert_vals)

        mysql_pandas = pd.read_sql('SELECT * FROM Transaction_log WHERE account_num = ' + account_num + ";", con=mysql_conn)
        print(mysql_pandas.head())
        mysql_pandas = pd.read_sql('SELECT * FROM Transaction_log WHERE account_num = ' + account_num + ";", con=mysql_conn)
        print(mysql_pandas.head())
    else:
        print("You must have accidentally NOT typed yes or no to get here...")
        print("Hopefully you didn't say no 4 times... ;)  ")


def view_Customers(ListOfCons):
    mysql_cur = ListOfCons[0]
    mysql_conn = ListOfCons[1]
    print("Please purview the data: ")
    mysql_pandas = pd.read_sql('SELECT * FROM Customer;', con=mysql_conn)
    print(mysql_pandas.head())

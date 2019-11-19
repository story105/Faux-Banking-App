import pymysql
import sqlite3
import pandas as pd
from random import randint

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
    return(mysql_cur)

#Change this name to SIGN_up / sign_in (break apart the stuff inside)
# table names: Account, Account_xref, Customer, Transaction_log
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


def Create_New_Customer():

    mysql_cur = Create_Connection()

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
                             VALUES (?,?,?,?)'''
    insert_vals = (customer_ID, SSN, FN, LN)
    print(insert_vals)
    print(type(customer_ID))
    print(type(SSN))
    print(type(FN))
    print(type(LN))
    print("")
    mysql_cur.execute(insert_sql, insert_vals)

    #WHERE customer_id =
    mysql_pandas = pd.read_sql('SELECT * FROM Customer;', con=mysql_conn)
    print(mysql_pandas.head())

    print("Please review your information above. ")
    print("")

def Create_Account():

    mysql_cur = Create_Connection()

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
            input_cash = int(input())
        except:
            print("Invalid Input. Adding base amount $420 ")
            input_cash = 420
    else:
        print("Couldn't decipher your request. Transferring $69 pity dollars to your {0} account.".format(account_type))

    account_num = randint(0, 9999999999)

    insert_sql = '''INSERT INTO Account(account_num, account_type, balance)
                             VALUES (?,?,?)'''
    insert_vals = (account_num, account_type, input_cash) # input cash == balance

    mysql_cur.execute(insert_sql, insert_vals)

    mysql_pandas = pd.read_sql('SELECT * FROM Account;', con=mysql_conn)
    print(mysql_pandas.head())

    print("Please review Account information above. ")
    print("")

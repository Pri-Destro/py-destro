import mysql.connector
from random import randrange
from datetime import date 
from time import sleep

user_acc = int()

# Creating Table Variables 
table1 = (
            'USE bank1;'
            "CREATE TABLE acc_detail("
            "acc_no int(15) primary key,"
            "name char(20),"
            "identity_no int(10),"
            "pin int(5),"
            "balance int(10));")
table2 = (
            'USE bank1;'
            "CREATE TABLE history("
            "acc_no int(15),"
            "deposited int(10),"
            "withdrawn int(10),"
            "transferred int(10),"
            "reciever int(15)"
            "date date,"
            "FOREIGN KEY (acc_no) REFERENCES acc_detail(acc_no));")

# Creating Database
cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234')
cursor = cnx.cursor()

try:
    cursor.execute('create database bank1')
except Exception:
    cursor.execute('use bank1')

try:
    cursor.execute(table1)
except Exception:
    cursor.execute('use bank1')

# Main Function
def main():
    print('\t ---------------------------------------------------------------------------------------')
    print('\t ***************************************************************************************')
    print('\t \t WELCOME TO PRI-BANK , PLEASE CHOOSE YOUR OPTION')
    print('\t \t 1. Create an account')
    print('\t \t 2. Banking')
    print('\t \t 3. EXIT')

    choice =int(input('choose --> '))
    while True:
        if choice == 1:
            creator()
            break
        elif choice == 2:
            banking()
            break
        elif choice == 3:
            cursor.close()
            cnx.close()
            exit()
        else:
            print('\t \t INVALID INPUT')
            main()

def banking():                                                                         
    global table2,user_acc
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    try:
        cursor.execute(table2)
    except Exception:
        cursor.execute('use bank1;')    
    print('\t ***************************************************************************************')
    print('\t ---------------------------------------------------------------------------------------')
    ask_acc()
    print('1. Deposit Cash')
    print('2. Withdraw Cash')
    print('3. Account Details')
    print('4. Transfer Money')
    print('***************************************************************************************')
    print('---------------------------------------------------------------------------------------')

    choice = int(input('Choose  -->  '))

    if choice == 1:
        deposit(user_acc)
    elif choice == 2:
        withdraw()
    elif choice == 3:
        details()
    elif choice == 4:
        transfer()
    else:
        print('INVALID INPUT!')


def deposit(acc):                               # Depositing Money
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    amount = int(input('Enter amount to be deposit --> '))
    txn_date = str(date.today())
    cursor.execute("insert into history (acc_no,deposited,date) values({},{},'{}');".format(acc,amount,txn_date))
    cursor.execute('update acc_detail set balance=balance+{} where acc_no={};'.format(amount,acc))
    cnx.commit()
    print('\t \t AMOUNT DEPOSITED')
    sleep(2)
    main()
    
    


def withdraw():                     # Withdrawing Money
    global user_acc
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    amount = int(input('Enter amount to be withdrawn --> '))
    txn_date = str(date.today())
    cursor.execute("insert into history (acc_no,withdrawn,date) values({},{},'{}');".format(user_acc,amount,txn_date))
    cursor.execute('update acc_detail set balance=balance-{} where acc_no={};'.format(amount,user_acc))
    cnx.commit()
    print('\t \t AMOUNT WITHDRAWN')
    sleep(2)
    main()

    
def transfer():                 # Transferring Money
    global user_acc
    reciever_acc = int(input("Enter reciever's account no --> "))
    amount = int(input('Enter amount to be transfer --> '))
    txn_date = str(date.today())
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    cursor.execute('select acc_no from acc_detail where acc_no={};'.format(reciever_acc))
    data = cursor.fetchone()
    if data is not None:
        print('Account Confirmed')
    else:
        print('Please input valid account number ')
    cursor.execute("insert into history (acc_no,transferred,reciever,date) values({},{},{},'{}');".format(user_acc,amount,reciever_acc,txn_date))
    cursor.execute('update acc_detail set balance=balance-{} where acc_no={};'.format(amount,user_acc))
    cnx.commit()
    deposit(reciever_acc)
    print('\t \t AMOUNT Transferred')
    sleep(2)
    main()


def ask_acc():                              # Checking if account exists
    global user_acc
    user_acc = int(input('Enter your Account Number --> '))
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    cursor.execute('SELECT acc_no FROM acc_detail where acc_no={};'.format(user_acc))
    acc = cursor.fetchone()
    if acc is not None:
        security()
    else:
        print('\t \t \t OOPS!!')
        print('\t \t \t PLEASE CREATE AN ACCOUNT FIRST')
        main()
            
def creator():                      # Creating a new account
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    acc_no = randrange(10000000,999999999)
    pin = randrange(1000,9999)
    print('######################################################################################')
    name = input('Enter Your Name --> ')
    identity_no = int(input('Enter Your Identity Number (8 DIGITS) --> '))
    print('---------------------------------------------------------------------------------------')
    print('***************************************************************************************')
    print('YOUR ACCOUNT NUMBER IS --> {}'.format(acc_no))
    print('YOUR SECRET PIN IS --> {} '.format(pin))
    amount = int(input('Enter amount to be deposit --> '))
    insert = ("insert into acc_detail values(%s,%s,%s,%s,%s);")
    val = (acc_no,name,identity_no,pin,amount)
    cursor.execute(insert,val)
    cnx.commit()
    print('Account Created !')
    main()

def details():                  # Details of a account
    global user_acc
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    cursor.execute('select * from acc_detail where acc_no={};'.format(user_acc))
    acc_datalist = cursor.fetchall()
    for data1 in acc_datalist:
        print('####################################################################################')
        print('\t \t YOUR ACCOUNT NUMBER --> {}'.format(data1[0]))
        print('\t \t YOUR Name --> {}'.format(data1[1]))
        print('\t \t YOUR IDENTITY NUMBER --> {}'.format(data1[2]))
        print('\t \t YOUR Balance --> {}'.format(data1[4]))
    cursor.execute('select * from history where acc_no={}'.format(user_acc))
    hist_datalist = cursor.fetchall()
    for data2 in hist_datalist:
        print('\t \t YOU DEPOSITED --> {}'.format(data2[1]))
        print('\t \t YOU WITHDRAWN --> {}'.format(data2[2]))
        print('\t \t MONEY TRANSFERRED --> {}'.format(data2[3]))
        print('\t \t ON DATE --> {}'.format(data2[4]))
        print('\t \t MONEY TRANSFERRED TO --> {}'.format(data2[5]))
        print('####################################################################################')
    sleep(4)
    main()
        
def security():                 # Checking if pin is correct
    cnx = mysql.connector.connect(user = 'root',host = 'localhost',passwd ='1234',database = 'bank1')
    cursor = cnx.cursor()
    sql = ('SELECT pin FROM acc_detail WHERE acc_no={}'.format(user_acc))
    cursor.execute(sql)
    pin_list = cursor.fetchall()
    user_pin = int(input('Enter Your Secret Pin --> '))
    for pins in pin_list:
        for j in pins:
            valid_pin = j
        if valid_pin == user_pin:
            break
        else:
            print('You Entered Wrong Pin')
            main()

main()
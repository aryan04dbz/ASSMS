import mysql.connector as sql_con
import random
from prettytable import PrettyTable

def inTerminalSelection(question_string : str, option_list : list):
    ''' This function handles the user input in terminal provided with options '''
    while True:
        print(question_string)
        for items in option_list:
            print(str(option_list.index(items)) + ".  "+ items)

        user_choice = input("Enter your choice : ")
        try:
            user_choice = int(user_choice)
            if user_choice < len(option_list):
                return user_choice
        except Exception as error:
            print("Please Enter the choice in correct format")
            continue

def view(): 
    search_q = inTerminalSelection("Do you want to see all the registry or search in them : ", ["All", "Search"])
    if search_q == 0: 
        cursor.execute("SELECT * FROM customer_details")

        Customer_data = PrettyTable()
        Customer_data.field_names = [
            'ID', 'CNAME', "ADDRESS", 'PH_NO', 'EMAIL', 'DL_NO', 'VEHICLE_NO', 'SCHEDULE_DATE',
            'SCHEDULE_TIME', 'SCHEDULE_DURATION', 'SERVICE_TYPE'
        ]
        for items in cursor.fetchall():
            Customer_data.add_row([
                items[0], 
                items[1], 
                items[2], 
                items[3], 
                items[4], 
                items[5],
                items[6],
                items[7], 
                items[8],
                items[9], 
                items[10]
            ])
        print(Customer_data, "\n\n")
            
    elif search_q == 1:
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME =  N'POST'")
        field_name = [
                'ID',
                'CNAME', 
                "ADDRESS", 
                'PH_NO',
                'EMAIL',
                'DL_NO',
                'VEHICLE_NO',
                'SCHEDULE_DATE',
                'SCHEDULE_TIME',
                'SCHEDULE_DURATION',
                'SERVICE_TYPE'
        ]
        user_choice = inTerminalSelection("Enter Field Name : ", field_name)
        
        query = input("Enter value : ")
        cursor.execute(f"SELECT * FROM customer_details WHERE {field_name[user_choice]}='{query}';")
        values = cursor.fetchall()
        if len(values) == 0:
            print("No Such Registry Exists")
            return 

        Customer_data = PrettyTable()
        Customer_data.field_names = [
            'ID', 'CNAME', "ADDRESS", 'PH_NO', 'EMAIL', 'DL_NO', 'VEHICLE_NO', 'SCHEDULE_DATE',
            'SCHEDULE_TIME', 'SCHEDULE_DURATION', 'SERVICE_TYPE'
        ]
        for items in values:
            Customer_data.add_row([
                items[0], 
                items[1], 
                items[2], 
                items[3], 
                items[4], 
                items[5],
                items[6],
                items[7], 
                items[8],
                items[9], 
                items[10]
            ])
        print(Customer_data, "\n\n")
        
    else: pass

def databaseConnection():
    global conn
    conn = sql_con.connect(host='localhost', user='root', passwd='Aryan04dbz@05', database='assms')
    
    if not conn.is_connected():
        print("Unable to connect to database, please take necessary steps. ")
        exit()  
    else:
        print("Connection Successful... ")
    
    global cursor 
    cursor = conn.cursor(buffered=True)

def randomIDGenerator(staff = False, customer = False):
    while True:
        random_ID = ""
        random_integer = random.randint(4, 10)
        
        for items in range(random_integer):
            random_ID += str(random.randint(0, 9))

        # if staff:
        #     cursor.execute(f"SELECT * FROM staffdatabase WHERE ID='{random_ID}'")
        # if customer:
        #     cursor.execute(f"SELECT * FROM customer_details WHERE ID='{random_ID}'")
        
        # cursorFetchall = cursor.fetchall()

        # print(cursorFetchall, type(cursorFetchall))
        
        return int(random_ID)

def logsign():
    """ This funtion handles Login and SignUp"""
    # Define the login function
    def login():
        # Prompt the user to enter their username and password

        logged_in = False

        while not logged_in:
            username = input('Enter your username: ')
            password = input('Enter your password: ')


            cursor.execute(f"SELECT * FROM staffdatabase WHERE USERNAME='{username}' AND PASSWD='{password}'")
            
            if len(cursor.fetchall()) != 0: logged_in = True; return 
            else:
                print("Invalid User Please Start The Program Again. Sorry For Inconvinience ! ") 
        
    def sign_up():
        # Prompt the user to enter a new username and password
        sname = input("Enter your name : ")
        address = input("Enter your address : ")
        email = input("Enter your email : ")
        username = input('Enter a new username: ')
        password = input('Enter a new password: ')

        sql_query = f"""
            INSERT INTO staffdatabase(
                    ID, 
                    SNAME,
                    ADDRESS, 
                    EMAIL,
                    USERNAME, 
                    PASSWD
                ) VALUES (
                    {randomIDGenerator(staff=True)}, 
                    '{sname}', 
                    '{address}',  
                    '{email}', 
                    '{username}', 
                    '{password}'
                )
        """
        cursor.execute(sql_query)
        conn.commit()
        print("SignUp Successfull ! ", "Welcome to management department !")

    question = "Login to existing account Or SingUp To Create Account : "
    choice = inTerminalSelection(question, ['Login', 'SignUp'])

    if choice == 0:
        login()
    elif choice == 1:
        sign_up()
    else:
        print('Invalid choice')

def task(option):

    def register():
        name = input("ENTER CUSTOMER'S NAME - ") 
        addrs = input("ENTER CUSTOMER'S ADDRESS - ")
        ph = input("ENTER THE CUSTOMER'S PHONE NUMBER - ")
        email = input("ENTER THE CUSTOMER'S EMAIL ADDRESS - ")
        dl = input("ENTER THE CUSTOMER'S DRIVING LICENSE NO - ")
        vno = input("ENTER CUSTOMER'S VEHICLE NUMBER - ")
        S_D = input("ENTER THE DATE OF THE SERVICE (DD/MM/YYYY)-  ")
        S_T = input("ENTER THE TIME OF THE SERVICE (HH:MM)- ")
        S_DU = input("ENTER THE DURATION OF THE SERVICE - ")
        S_TYPE = input("ENTER WHAT TYPE OF SERVICE IS TO BE DONE - ")
        sql_query = f''' INSERT INTO customer_details(
                ID,
                CNAME, 
                ADDRESS, 
                PH_NO,
                EMAIL,
                DL_NO,
                VEHICLE_NO,
                SCHEDULE_DATE,
                SCHEDULE_TIME,
                SCHEDULE_DURATION,
                SERVICE_TYPE
            ) 
                VALUES(
                    {randomIDGenerator()}, 
                    '{name}', 
                    '{addrs}', 
                    '{ph}', 
                    '{email}', 
                    '{dl}', 
                    '{vno}',
                    '{S_D}',
                    '{S_T}',
                    {S_DU},
                    '{S_TYPE}'
                );
        '''
        cursor.execute(sql_query)
        conn.commit()
        print("User Added Successfully. \n\n")

    if option==1: 
        register()
    elif option==2: pass
    elif option==3: pass
    elif option==4: pass
    else: print("Internal Error")
        
def main():
    databaseConnection()
    logsign()

    run = True 
    print("--------------------------------------")
    print("Welcome to the Automobile Service Station Management System")
    print("--------------------------------------")
    
    while run:
        
        print("1. Add New Customer")
        print("2. Schedule")
        print("3. Search")
        print("4. Exit")
       
        choice = int(input("Enter the Choice - "))
        if choice == 1:
            task(choice)
        elif choice == 2:
            schedule("update")
        elif choice == 3:
            view()
        else:
            print("PLEASE INPUT THE CORRECT CHOICE")
            


        question = "Do you want to run the program again ?"
        choice = ['Yes', 'No']
        user_choice = inTerminalSelection(question, choice)
        if user_choice == 1: 
            exit()

def schedule(choice):

    I_ID = input("ENTER THE ID OF THE CUSTOMER - ")
    S_D = input("ENTER THE DATE OF THE SERVICE (DD/MM/YYYY)-  ")
    S_T = input("ENTER THE TIME OF THE SERVICE (HH:MM)- ")
    S_DU = input("ENTER THE DURATION OF THE SERVICE - ")
    S_TYPE = input("ENTER WHAT TYPE OF SERVICE IS TO BE DONE - ")
    if choice == "update":
        sql_query = f""" 
                        UPDATE customer_details 
                        SET SCHEDULE_DATE = '{S_D}',
                        SCHEDULE_TIME = '{S_T}', 
                        SCHEDULE_DURATION = {int(S_DU)}, 
                        SERVICE_TYPE = '{S_TYPE}' WHERE ID='{I_ID}';
                    """
    cursor.execute(sql_query)
    conn.commit()

main()




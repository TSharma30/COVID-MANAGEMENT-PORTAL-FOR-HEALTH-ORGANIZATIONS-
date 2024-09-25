import mysql.connector
import T
mydb = mysql.connector.connect(host="localhost", user="root", passwd="tarun123")
mycursor = mydb.cursor()
mydb.autocommit = True


#CREATING DATABASE
mycursor.execute("create database if not exists covid_management")
mycursor.execute("use covid_management")


#CREATING TABLES
mycursor.execute("create table if not exists staff(sno varchar(25) not null,name varchar(25) not null,age varchar(25) not null,gender varchar(8) not null, post varchar(25) not null,salary varchar(25) not null)")
mycursor.execute("create table if not exists patients(sno varchar(25) not null,name varchar(25) not null,age varchar(25) not null,gender varchar(25) not null,date date not null)")
mycursor.execute("create table if not exists login(admin varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists sno(patient varchar(25) not null,staff varchar(25) not null)")


#FOR NEW SYSTEM AUR ADMIN

mycursor.execute("select * from sno")
z = 0
for i in mycursor:
    z=1
if z==0:
    mycursor.execute("insert into sno values('0','0')")

mycursor.execute("select * from login")
j = 0
for i in mycursor:
    j=1
if j==0:
        print("\t\t\t\t~~~~~~~~~~~~~~~~~~~~")
        print("\t\t\t\t~CREATE NEW ACCOUNT~  ")
        print("\t\t\t\t~~~~~~~~~~~~~~~~~~~~")
        username = input("Enter your Username  : ")
        pwd = input("Enter your password  : ")
        cpwd = input("Confirm your password : ")
        sql =("insert into login (admin,password) values ('"+username+"', '"+str(cpwd)+"') ")
        mycursor.execute(sql)
        print('\n!!! User ID successfully created !!!\n')

        
#REGISTRATION

def login():
    print("\t\t\t\t~~~~~~~~~~~~")
    print("\t\t\t\t    LOGIN")
    print("\t\t\t\t~~~~~~~~~~~~")
    username=input('Enter your Username:   ')
    pwd=input('Enter your password:   ')
    mycursor.execute('select * from login where admin="'+username+'"and password="'+pwd+'";')
    x=mycursor.fetchone()
    if (username,pwd)==x:
        print("\n\t\t\t   ~~~~~~~~~~~~~~~~~~~~~")
        print('\n\t\t\t      LOGIN SUCCESSFUL\n')
        print("\t\t\t   ~~~~~~~~~~~~~~~~~~~~~\n")
        return True  

    else:
        print('\nError in given data\n')

def change_password():
    pas = input("Enter Old password: ")
    mycursor.execute("select * from login")
    for i in mycursor:
        username,password=i
    if (pas==password):
        npas=input("Enter New Password: ")
        cpas=input("Confirm New Password: ")
        mycursor.execute("update login set password='"+cpas+"'")
        mydb.commit()
        print("\nPassword successfully changed.")
    else:
        print("The password is incorrect.")
        

#MENU DRIVEN PROGRAM
        
l1 = 'y'
while (l1.upper()=='Y'):
    print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t  COVID MANAGEMENT PORTAL FOR HEALTH ORGANIZATIONS ")
    print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n\t\t\t    ****************************")
    print("\t\t\t    |   1.REGISTERED USER      |")
    print("\t\t\t    |   2.SELF-ASSESSMENT TEST |")
    print("\t\t\t    |   3.EXIT                 |")
    print("\t\t\t    ****************************\n")

    ch1 = int(input("Enter your choice: "))
    if(ch1 == 1):
        enter = login()
        if enter:
            l2 = 'y'
            while (l2.upper()=='Y'):
                print("\t\t    **********************************")
                print("\t\t    |  1.ADD PATIENTS                |")              
                print("\t\t    |  2.ADD STAFF                   |")
                print("\t\t    |  3.DISPLAY PATIENTS RECORD     |")
                print("\t\t    |  4.DISPLAY STAFF RECORD        |")
                print("\t\t    |  5.CHANGE PASSWORD             |")
                print("\t\t    |  6.REMOVE PATIENTS             |")
                print("\t\t    |  7.REMOVE STAFF                |")
                print("\t\t    |  8.COVID-19 PRECAUTIONS        |")
                print("\t\t    |  9.LOGOUT                      |")
                print("\t\t    **********************************\n")

                ch2 = int(input("Enter your choice: "))

                if (ch2 == 1):
                    l3 = 'y'
                    while (l3.upper()=='Y'):
                        T.add_patient()
                        l3 = input("\nDo you want to Enter More Data..(Y/N): ")

                elif (ch2 == 2):
                    l3 = 'y'
                    while (l3.upper()=='Y'):
                        T.add_staff()
                        l3 = input("\nDo you want to Enter More Data..(Y/N): ")

                elif (ch2 == 3):
                    l3 = 'y'
                    while (l3.upper()=='Y'):
                        T.display_patients_record()
                        l3 = input("\nDo you want to display more Patient Records..(Y/N): ")

                elif (ch2 == 4):
                    l3 = 'y'
                    while(l3.upper()=='Y'):
                        T.display_staff_record()
                        l3=input("\nDo you want to display more Staff Records..(Y/N): ")

                elif (ch2 == 5):
                    change_password()

                elif (ch2 == 6):
                    l3 = 'y'
                    while (l3.upper()=='Y'):
                        T.remove_patient()
                        l3 = input("\nDo you want to Remove More Patients..(Y/N): ")

                elif (ch2 == 7):
                    l3 = 'y'
                    while (l3.upper()=='Y'):
                        T.remove_staff()
                        l3 = input("\nDo you want to Remove More Staff..(Y/N): ")

                elif (ch2 == 9):
                    cnf=input("ARE YOU SURE YOU WANT TO LOG OUT (Y/N): ").lower()
                    if (cnf=='y'):
                        print("\nUSER SUCCESSFULLY LOGGED OUT\n")
                        break
                                    
                        

                elif (ch2 == 8):
                    print("""\nTo prevent the spread of COVID-19:
\n a) Clean your hands often. Use soap and water, or an alcohol-based hand rub.
\n b) Maintain a safe distance from anyone who is coughing or sneezing.
\n c) Wear a mask when physical distancing is not possible.
\n d) Don’t touch your eyes, nose or mouth.
\n e) Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
\n f) Stay home if you feel unwell.
\n g)If you have a fever, cough and difficulty breathing, seek medical attention.\n""")
                

                l2 = input("\nDo you want to Continue..(Y/N): ")

    elif (ch1 == 2):
        T.test()

    elif (ch1 == 3):
        cexit=input("ARE YOU SURE YOU WANT TO EXIT(Y/N): ").lower()
        if (cexit == "y"):
            print("THANK YOU FOR LOGGING IN, STAY HOME STAY SAFE :)")
            break
        else:
            l2 = input("\nDo you want to Continue..(Y/N): ")
            
            



















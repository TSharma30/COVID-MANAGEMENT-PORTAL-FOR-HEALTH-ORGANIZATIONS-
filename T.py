import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="tarun123")
mycursor = mydb.cursor()
mydb.autocommit = True
mycursor.execute("create database if not exists covid_management")
mycursor.execute("use covid_management")


def add_patient():
    name = input("\nEnter patients name: ")
    age = int(input("Enter patients age: "))
    gender = input("Enter patients gender(m/f): ")
    date = input("Enter date of confirmation of covid: ")
    mycursor.execute("select * from sno")
    for i in mycursor:
        patient, staff=i
        patient = int(patient) + 1

    mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+str(age)+"','"+gender+"','"+date+"')")


    mycursor.execute("update sno set patient='"+str(patient)+"'")
    mydb.commit()
    print("\nData of Patient has been saved successfully!!\n")
    mycursor.execute("select * from patients")
    t=0
    for i in mycursor:
        t+=1
        t_id1,name1,age1,gender1,date1=i
    print(f"Total number of Corona infected  patients: {patient}\n")

    print(f"Active Corona cases: {t}\n")

    print(f"This patient with id {t_id1} will be quarantine upto 14 days from {date1}")


    

def add_staff():
    name = input("\nEnter staff name: ")
    age = input("Enter age: ")
    gender=input("Enter gender(m/f): ")
    post = input("Enter his/her post: ")
    salary = input("Enter his/her Salary: ")

    mycursor.execute("select * from sno")
    for i in mycursor:
        patient,staff=i
        staff=int(staff)+1
    mycursor.execute("insert into staff values('"+str(staff)+"','"+name+"','"+age+"','"+gender+"','"+post+"','"+salary+"')")
    mycursor.execute("update sno set staff='"+str(staff)+"'")
    mydb.commit()
    print(f"Staff with id(staff) has been saved successfully..")
    mycursor.execute("select * from staff")
    t=0
    for i in mycursor:
        t+=1
    print(f"\nActive staff members: {t}\n")

    
    
def display_patients_record():
        idd = input("\nEnter Patient's ID: ")
        t_id2,name2,age2,gender2,date2=["", "", "", "", ""]
        mycursor.execute("select * from patients where sno = '"+idd+"'")
        for i in mycursor:
                t_id2,name2,age2,gender2,date2=i
        print("| ID | NAME | AGE | GENDER | CORONA POSITIVE DATE |")
        print(f" | {t_id2} | {name2} | {age2} | {gender2} | {date2} |")



def display_staff_record():
        idd = input("\nEnter Staff ID: ")
        t_id3,name3,age3,gender3,past3,salary3=["", "", "", "", "", ""]
        mydb.commit()
        mycursor.execute("select * from staff where sno = '"+idd+"'")
        for i in mycursor:
                t_id3,name3,age3,gender3,past3,salary3=i
        print("| ID | NAME | AGE | GENDER | POST | SALARY |")
        print(f" | {t_id3} | {name3} | {age3} | {gender3} | {past3} | {salary3} |")



def remove_patient():
        idd = input("\nEnter Patient ID: ")
        mycursor.execute("delete from patients where sno = '"+idd+"'")
        mydb.commit()
        print("Patient has been removed successfully")



def remove_staff():
        idd = input("\nEnter Staff ID: ")
        mycursor.execute("delete from Staff where sno = '"+idd+"'")
        mydb.commit()
        print("Staff has been removed successfully")




def test():
    print("Thank you for coming forward for your test")
    icough=input("Are you feeling cough?(y/n): ").lower()   #Y-->y
    dry_cough = "n"
    cough = "n"
    
    if(icough == 'y' or icough == 'Y'):
        dry_cough = input("Are you feeling dry cough(y/n): ").lower()
        cough= input("Are you feeling wet cough(y/n): ").lower()
        
    sneeze=input("Are you feeling sneeze?(y/n): ").lower()
    pain=input("Are you feeling pain in your body?(y/n): ").lower()
    weakness=input("Are you feeling weakness?(y/n): ").lower()
    mucus=input("Are you feeling mucus?(y/n): ").lower()
    
    itemp=int(input("Please enter your temprature: "))
    if(itemp<=100):
        temp="low"                      #low = <98
    else:
        temp="high"                     #high = >98
        
    breath=input("Are you facing difficulty in breathing(y/n): ").lower()
    
    if (dry_cough=='y'and sneeze=='y'and pain=='y'and weakness=='y'and mucus=='y' and temp =='high' and breath=='y'):
        print("\n\nSORRY BUT ACCORDING TO THE ABOVE TEST RESULTS YOU ARE SUFFERING FROM COVID-19")
        print("YOU ARE ADVISED TO BE IN SELF ISOLATION AS SOON AS POSSIBLE")
        print("PLEASE CONTACT THE HEALTH SERVICES")
        print("HELPLINE NUMBER: +91-11-23978046")
        print("TOLL FREE: 1075")
        print("HELPLINE E-MAIL ID: ncov2019@gmail.com\n\n")    
        
        name=input("Enter your name: ")                             #TAKES YOUR INFO. AND SAVES IT TO THE DATABASE
        age=int(input("Enter your age: "))
        gender=input("Enter your gender(m/f): ")


        mycursor.execute("select * from sno")
        for i in mycursor:
            patient,staff=i
            patient=int(patient)+1
        mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+str(age)+"','"+gender+"',now())")
        mycursor.execute("update sno set patient='"+str(patient)+"'")
        mydb.commit()
        print("Data of Patient has been saved successfully!!")
        print(f"Total number of Corona infected patients: {patient}\n")
        mycursor.execute("select * from patients")
        
        #runs through the records and count them
        
        t=0
        for i in mycursor:
            t+=1
        print(f"Active Corona Cases are: {t}")
        
        mycursor.execute("Select * from patients")
        for i in mycursor:
            t_id5,name5,age5,gender5,date5=i
        print(f"This patient with id {t_id5} will be in quarantine for upto 14 days from {date5}")
        
    elif(dry_cough == 'y' and sneeze == 'y' and pain == 'n' and weakness == 'n' and temp == 'low' and breath == 'n'):
        print("\nNothing to worry, its just due to Air Pollution :) STAY HOME, STAY SAFE \n") 

    elif(cough == 'y' and mucus == 'y' and sneeze == 'y' and pain == 'n' and weakness == 'n' and temp == 'low' and breath == 'n'):
        print("\nNothing to worry its just Common Cold :) STAY HOME, STAY SAFE \n")

    else:
        print("\nYou are not Corona infected, if you are not feeling well you just need to rest :)\n")
        print("Still if you can't feel better, please consult doctor asap \n!!")

   


        
    




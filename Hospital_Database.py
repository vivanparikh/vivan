'''
HEADER:
This is the main.py file 

⨀File name specifications: Hospital_Database.py
⨀Date and Time format of the File – YYYYMMDD, HHMMSSTT

⨀Header Records Layout –
|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active

⨀Details Record Layout – 
|D|John|123456|2010-10-12|2012-10-13|MVD|Paul|NSW|AU|06031987|A

⨀Python Version: 3.8 or 3.9
⨀MySql version: 8.0 and above

Thankyou :)

'''

import Menus
import TableAccess as TA

print('__________________________________________________________________________________________________________')
Menus.start_screen()

while True:
    Menus.MainMenu()
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        while True:
            Menus.MENUi()
            choice10=int(input("Enter you choice: "))

            if (choice10==1):
                TA.INS('Main_Table','Table_India')
            elif(choice10==2):
                TA.UPD('Main_Table','Table_India')
            elif(choice10==3):
                TA.DIS('Table_India')
            elif(choice10==4):
                TA.DEL('Main_Table','Table_India')
            elif(choice10==5):
                print("\n\t|Going to Main Menu|")
                break
            else:
                print("\t|Invalid Input, Please Try Again|")

    elif choice==2:
        while True:
            Menus.MENUi()
            choice20=int(input("Enter you choice: "))

            if (choice20==1):
                TA.INS('Main_Table','Table_USA')
            elif(choice20==2):
                TA.UPD('Main_Table','Table_USA')
            elif(choice20==3):
                TA.DIS('Table_USA')
            elif(choice20==4):
                TA.DEL('Main_Table','Table_USA')
            elif(choice20==5):
                print("\n\t|Going to Main Menu|")
                break
            else:
                print("\t|Invalid Input, Please Try Again|")

    elif choice==3:
        while True:
            Menus.MENUi()
            choice30=int(input("Enter you choice: "))

            if (choice30==1):
                TA.INS('Main_Table','Table_Phil')
            elif(choice30==2):
                TA.UPD('Main_Table','Table_Phil')
            elif(choice30==3):
                TA.DIS('Table_Phil')
            elif(choice30==4):
                TA.DEL('Main_Table','Table_Phil')
            elif(choice30==5):
                print("\n\t|Going to Main Menu|")
                break
            else:
                print("\t|Invalid Input, Please Try Again|")

    elif choice==4:
        while True:
            Menus.MENUi()
            choice40=int(input("Enter you choice: "))

            if (choice40==1):
                TA.INS('Main_Table','Table_NYC')
            elif(choice40==2):
                TA.UPD('Main_Table','Table_NYC')
            elif(choice40==3):
                TA.DIS('Table_NYC')
            elif(choice40==4):
                TA.DEL('Main_Table','Table_NYC')
            elif(choice40==5):
                print("\n\t|Going to Main Menu|")
                break
            else:
                print("\t|Invalid Input, Please Try Again|")

    elif choice==5:
        while True:
            Menus.MENUi()
            choice50=int(input("Enter you choice: "))

            if (choice50==1):
                TA.INS('Main_Table','Table_AU')
            elif(choice50==2):
                TA.UPD('Main_Table','Table_AU')
            elif(choice50==3):
                TA.DIS('Table_AU')
            elif(choice50==4):
                TA.DEL('Main_Table','Table_AU')
            elif(choice50==5):
                print("\n\t|Going to Main Menu|")
                break
            else:
                print("\t|Invalid Input, Please Try Again|")

    elif choice==6:
        TA.DIS('Main_Table')

    elif choice==8:
        print("\n\t||EXITING||")
        break

    else:
        print("\t|Invalid Input, Please Try Again|")

print('__________________________________________________________________________________________________________')

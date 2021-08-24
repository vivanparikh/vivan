"""
This File has the program for executing the queries raised for Sql with python as the front End
"""

import mysql.connector as m
import Menus 

password=str(input("\nEnter your Database password: "))
db=m.connect(host='localhost',user='root',passwd=password)

if db.is_connected():                                   #To Check the Connection Status
    print('\t|Connection established|')
    c=db.cursor()
    c.execute('create database if not exists HOSPITAL')
    c.execute('use HOSPITAL')

    def INS(tname1,tname2):                             #To Insert A Row
        try: 
            print('')
            k=int(input('Enter the no. of rows you want to add: '))
            print('')

            for i in range(0,k):
                c_name=str(input("Enter the Customer Name: "))
                c_id=str(input("Enter the Customer Id: "))
                c_od=str(input("Enter the Open Date: "))
                c_lcd=str(input("Enter the Last Consulted Date: "))
                v_type=str(input("Enter the Vaccination Type: "))
                doc=str(input('Enter the Doctor Consulted: '))
                state=str(input('Enter the State: '))
                cou=str(input('Enter the Country: '))
                p_code=str(input('Enter the Post Code: '))
                dob=str(input('Enter the Date Of Birth: '))
                c_act=str(input('Is the Customer Active?: '))
                
                query1="insert into "+tname1+" values('"+c_name+"','"+c_id+"','"+c_od+"','"+c_lcd+"','"+v_type+"','"+doc+"','"+state+"','"+cou+"','"+p_code+"','"+dob+"','"+c_act+"')"
                query2="insert into "+tname2+" values('"+c_name+"','"+c_id+"','"+c_od+"','"+c_lcd+"','"+v_type+"','"+doc+"','"+state+"','"+cou+"','"+p_code+"','"+dob+"','"+c_act+"')"

                c.execute(query1)
                db.commit()
                c.execute(query2)
                db.commit()
                print('')
                print('Data Inserted :)')
                print('')

        except :
            print('')
            print('\t|An error occurred|')
            print('The Customer Name you gave may already exist or you did not fill the mandatory details')
            print('')

        query3="select * from "+tname1+";"
        c.execute(query3)
        ans=c.fetchall()
        Heading1="\n|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|Post_Code|DOB|Is_Active|\n"
        f=open("_Hospital_Database.txt","w")
        f.write(Heading1)
        string1="|D|"
        if len(ans)>0:
            for i in ans:
                f=open("_Hospital_Database.txt","a")
                for j in range(11):
                    string1+=str(i[j])+'|'
                string1+="\n|D|"
            f.write(string1)
        else:
            print('')
        f.close()

    def DEL(tname1,tname2):                                          #To delete a row
        print('')
        k=int(input('Enter the no. of rows you want to Delete: '))
        print('')
        
        for i in range(0,k):
            c_id=str(input('Enter the Customer Id: '))
            query1="delete from "+tname1+" where Customer_Id='"+c_id+"'"
            query2="delete from "+tname2+" where Customer_Id='"+c_id+"'"
            c.execute(query1)
            db.commit()
            y=c.rowcount
            c.execute(query2)
            db.commit()
            x=c.rowcount

            if (x==0 or y==0):
                print('')
                print('An error occurred')
                print('ID you gave does not exist :( ')
                print('')

            else:
                query3="Customer Id '"+c_id+"' record successully deleted! "
                print('')
                print(query3)
                print('')

    def DIS(tname1):                                               #To display the table
        query1="select * from "+tname1+";"
        c.execute(query1)
        ans=c.fetchall()
        print('')
        if len(ans)<1:
            print("\t|No Data Exists|\n")
        else:
            Menus.Heading()
            for i in ans:
                print("\n|D",i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],sep='|')
            print('')

    def UPD(tname1,tname2):
        DIS(tname2)
        Id=str(input("Enter the Customer Id: "))

        ID_final='%'+Id+'%'
        ID_for_SQL=ID_final
        query1="select * from "+tname1+" where Customer_Id like '"+ID_for_SQL+"' "
        c.execute(query1)
        ans=c.fetchall()

        if len(ans)==0:
            print('')
            print('An error occurred due to input of non existing ID')
            print('Please try again')
            print('')

        else:   
            Menus.MENUii()
            colno=str(input('So, what will it be?: '))
            print('')

            if int(colno)==1:
                c_name=str(input('Enter the updated Name: '))
                query2="update "+tname1+" set Customer_Name='"+c_name+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Customer_Name='"+c_name+"' where Customer_Id='"+Id+"'"

            elif int(colno)==2:
                c_id=str(input('Enter the updated ID: '))
                query2="update "+tname1+" set Customer_Id='"+c_id+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Customer_Id='"+c_id+"' where Customer_Id='"+Id+"'"

            elif int(colno)==3:
                c_od=str(input('Enter the updated Open Date: '))
                query2="update "+tname1+" set Customer_Open_Date='"+c_od+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Customer_Open_Date='"+c_od+"' where Customer_Id='"+Id+"'"

            elif int(colno)==4:
                c_lcd=str(input('Enter the updated Last Consulted Date: '))
                query2="update "+tname1+" set Last_Consulted_Date='"+c_lcd+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Last_Consulted_Date='"+c_lcd+"' where Customer_Id='"+Id+"'"

            elif int(colno)==5:
                v_type=str(input('Enter the updated Vaccination ID: '))
                query2="update "+tname1+" set Vaccination_Type='"+v_type+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Vaccination_Type='"+v_type+"' where Customer_Id='"+Id+"'"

            elif int(colno)==6:
                doc=str(input('Enter the updated Doctor Consulted: '))
                query2="update "+tname1+" set Doctor_Consulted='"+doc+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Doctor_Consulted='"+doc+"' where Customer_Id='"+Id+"'"

            elif int(colno)==7:
                state=str(input('Enter the updated State: '))
                query2="update "+tname1+" set State='"+state+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set State='"+state+"' where Customer_Id='"+Id+"'"

            elif int(colno)==8:
                p_code=str(input('Enter the updated Post Code: '))
                query2="update "+tname1+" set Post_Codee='"+p_code+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Post_Codee='"+p_code+"' where Customer_Id='"+Id+"'"

            elif int(colno)==9:
                dob=str(input('Enter the updated Date Of Birth: '))
                query2="update "+tname1+" set Date_Of_Birth='"+dob+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Date_Of_Birth='"+dob+"' where Customer_Id='"+Id+"'"

            elif int(colno)==10:
                c_act=str(input('Enter the updated Status: '))
                query2="update "+tname1+" set Active_Customer='"+c_act+"' where Customer_Id='"+Id+"'"
                query3="update "+tname2+" set Active_Customer='"+c_act+"' where Customer_Id='"+Id+"'"

            else:
                print('The entered value is incorrect,please try again')

            c.execute(query2)
            db.commit()
            c.execute(query3)
            db.commit()
            print('')
            print('Updated :)')
            print('')

else:
    print("\t|Connection was not established, please try again|")


Database Name: HOSPITAL
Tables: 
(1)Main_Table    (2)Table_India     (3)Table_USA
(4)Table_Phil    (5)Table_NYC       (6)Table_AU

Hospital_Database.py: This is the main.py file.

MODULES:
(1)Menus.py: This file has the menus/texts used in the Hospital_Database.py
(2)TableAccess.py: This File has the program for executing the queries raised for Sql with python as the Front End.

QUERIES:
create database hospital;

use hospital;

create table Main_Table
(Customer_Name varchar(255) primary key,
Customer_Id varchar(18) not null,
Customer_Open_Date date not null,
Last_Consulted_Date date,
Vaccination_Type char(5),
Doctor_Consulted char(255),
State char(5),
Country char(5),
Post_Code int(5),
Date_Of_Birth date,
Active_Customer char(1));

create table Table_India
(Customer_Name varchar(255) primary key,
Customer_Id varchar(18) not null,
Customer_Open_Date date not null,
Last_Consulted_Date date,
Vaccination_Type char(5),
Doctor_Consulted char(255),
State char(5),
Country char(5),
Post_Code int(5),
Date_Of_Birth date,
Active_Customer char(1));

create table Table_USA
(Customer_Name varchar(255) primary key,
Customer_Id varchar(18) not null,
Customer_Open_Date date not null,
Last_Consulted_Date date,
Vaccination_Type char(5),
Doctor_Consulted char(255),
State char(5),
Country char(5),
Post_Code int(5),
Date_Of_Birth date,
Active_Customer char(1));

create table Table_Phil
(Customer_Name varchar(255) primary key,
Customer_Id varchar(18) not null,
Customer_Open_Date date not null,
Last_Consulted_Date date,
Vaccination_Type char(5),
Doctor_Consulted char(255),
State char(5),
Country char(5),
Post_Code int(5),
Date_Of_Birth date,
Active_Customer char(1));

create table Table_NYC
(Customer_Name varchar(255) primary key,
Customer_Id varchar(18) not null,
Customer_Open_Date date not null,
Last_Consulted_Date date,
Vaccination_Type char(5),
Doctor_Consulted char(255),
State char(5),
Country char(5),
Post_Code int(5),
Date_Of_Birth date,
Active_Customer char(1));

create table Table_AU
(Customer_Name varchar(255) primary key,
Customer_Id varchar(18) not null,
Customer_Open_Date date not null,
Last_Consulted_Date date,
Vaccination_Type char(5),
Doctor_Consulted char(255),
State char(5),
Country char(5),
Post_Code int(5),
Date_Of_Birth date,
Active_Customer char(1));



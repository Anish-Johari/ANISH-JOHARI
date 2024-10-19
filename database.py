'''Assignment No.: 19
Title: Write a programme to create a table employee with fields empid,empname varchar (20),
      employee address varchar(20),also insert 4 records using user input also insert 4 record buy user input.
Date:10/07/2023
Developed by: Anish Johari
_______________________________________'''
import mysql.connector as p
db=p.connect(host="localhost",
                user="root",
             password="Hanuman@_ji1971749905")
s=db.cursor()
s1="insert into employee values(%s,%s,%s)"
s.execute("create database if not exists school")
s.execute("use school")
s.execute("create table if not exists employee(emp_id int,emp_name varchar(20),emp_address varchar(70))")
for i in range(4):
                ec=int(input("Enter the employee code : "))
                en=input("Enter the name of the employee : ")
                ea=input("Enter the address of employee's residence : ")
                to=(ec,en,ea)
                s.execute(s1,to)
                db.commit()
print("Data successfully stored...")
s5="select * from employee"
s.execute(s5)
p=s.fetchall()
for i in p:
                print(i)

'''Assignment No.: 20
Title: Write a programme to display the data of employees whose name starts with P.
Date:17/07/2023
Developed by: Anish Johari
_______________________________________'''
import mysql.connector as p
db=p.connect(host="localhost",
             user="root",
             password="Hanuman@_ji1971749905")
cur=db.cursor()
s1="use school"
s2="Select * from employee where emp_name like 'p%' "
cur.execute(s1)
cur.execute(s2)
pr=cur.fetchall()
print("The record of employees whose name starts with p are \n\n")
for i in pr:
                print(i)

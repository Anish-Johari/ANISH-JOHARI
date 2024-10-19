'''Assignment No.: 22
Title: Write a programme to remove a data of an employee after searching on empid.
Date:07/08/2023
Developed by: Anish Johari
_______________________________________'''
import mysql.connector as p
db=p.connect(host="localhost",
             user="root",
             password="Hanuman@_ji1971749905")
cur=db.cursor()
s="use school"
cur.execute(s)
i=input("Enter the employee ID for removing the data: ")
s1="delete from employee where emp_id=%s"%(i,)
cur.execute(s1)
s2="select * from employee"
show=cur.execute(s2)
fetch=cur.fetchall()
for i in fetch:
                print(i)
print("\nData successfully removed...")

'''Assignment No.: 24
Title: Write a programme to update the information of an employee after searching on employee id.
Date:14/08/2023
Developed by: Anish Johari
_______________________________________'''
import mysql.connector as p
db=p.connect(host="localhost",
             user="root",
             password="Hanuman@_ji1971749905")
cur=db.cursor()
s1="use school"
cur.execute(s1)
emp_id=int(input("Enter the employee id who\'s record is to be updated :  "))
emp_name=input("Enter the new name of the employee: ")
emp_sal=input("Enter the new address of the employee: ")
selection1="UPDATE salary SET emp_name= %s WHERE emp_id= %s"%(emp_name,emp_id,)
selection2="update salary set emp_sal=%s where emp_id=%s"%(emp_sal,emp_id,)
cur.execute(selection1,val)
cur.execute(selection2)
db.commit()
selection3="Select* from employee"
cur.execute(selection3)
c=cur.fetchall()
print("The record has been updated...\n\nThe updated records are : \n\n ")
for i in c:
                print(i)

'''Assignment No.: 25
Title: Write a programme to display the data of employees ofter updating their salary by 20% hike.
Date:04/09/2023
Developed by: Anish Johari
_______________________________________'''
import mysql.connector as p
db=p.connect(host="localhost",
             user="root",
             password="Hanuman@_ji1971749905")
cur=db.cursor()
s1="use school"
cur.execute(s1)
s2="update salary set emp_sal=emp_sal+(20/100)*emp_sal"
cur.execute(s2)
db.commit()
s3="select employee.emp_id,employee.emp_name,emp_address,emp_sal from employee,salary where employee.emp_id=salary.emp_id"
cur.execute(s3)
s=cur.fetchall()
print("Salary of all the employees has been updated...\n\nThe records of employees with updated salary are : \n ")
for i in s:
                print(i)

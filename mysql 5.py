'''Assignment No.: 23
Title: Write a programme to display empid , empname empsal for all the employees
                create a table salary with fields empid and empsal.
Date:07/08/2023
Developed by: Anish Johari
_______________________________________'''
import mysql.connector as p
db=p.connect(host="localhost",
             user="root",
             password="Hanuman@_ji1971749905")
cur=db.cursor()
s1="use school"
cur.execute(s1)
s2="create table salary (emp_id int,emp_sal int)"
cur.execute(s2)
s3="insert into salary values(101,20000)"
s4="insert into salary values(102,25000)"
s5="insert into salary values(103,40000)"
s6="select employee.emp_id,emp_name,emp_sal from employee,salary where employee.emp_id=salary.emp_id"
cur.execute(s3)
cur.execute(s4)
cur.execute(s5)
db.commit()
cur.execute(s6)
py=cur.fetchall()
print("The data of all employee is: \n\n")
print("Employee ID,Employee name,Employee salary")
for i in py:
    print(i)

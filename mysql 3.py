'''Assignment No.: 21
Title: Write a programme to search for any employee on the basis of empid ,empname 
Date:24/07/2023
Developed by: Anish Johari
_______________________________________'''
import mysql.connector as p
db=p.connect(host="localhost",
             user="root",
             password="Hanuman@_ji1971749905")
cur=db.cursor()
s="use school"
cur.execute(s)
while True:
                print("1. Search on bases of employee ID.\n2. Search on bases of employee name.")
                s=int(input("Enter your choice : "))
                try:
                                if s==1:
                                                i=input("Enter the employee ID : ")
                                                s1="Select * from employee where emp_id=%s"%(i)
                                                cur.execute(s1)
                                                print("\n","The data of given value is:  ",cur.fetchall(),"\n")                                 
                                elif s==2:
                                                name=input("Enter the name of the employee")
                                                s2="select * from employee where emp_name='%s'"%(name,)
                                                cur.execute(s2)
                                                print("\n","The data of given value is: ",cur.fetchall(),"\n")                                                          
                except:
                                print("\nData doesn't found...\n")

'''Assignment No.: 16
title:Write a programme to create CSV file with data of 3 employees.
Date:17/04/2023
Developed by: Anish Johari
____________________________________'''
import csv
def CSV_FILE_WRITING():

    with open('Employees_data_in_CSV.csv','w',newline="") as sum:
        writes=csv.writer(sum)
        writes.writerow(["Identity_no","Name","salary","Email_id","Timeduration"])
        for i in range(3):
            name=input("Enter the name of the Employee:  ")
            identity=int(input("Enter the identity number of the employee:  "))
            Salary=int(input("Enter the package earned by the employee anually:  "))
            timeduration=int(input("Enter the time duration served in the company:  "))
            email_id=input("Enter the emailid of  the employee:  ")
            writes.writerow([identity,name,Salary,email_id,timeduration])
    sum.close()
    print("Data successfully stored in CSV file...")


CSV_FILE_WRITING()

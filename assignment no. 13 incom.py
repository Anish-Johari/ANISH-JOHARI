'''Assignment No.: 13
title:Write a programme to input the data and create a text file with data of employees .Show the data after reading the file.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
def Employee():
    f=open("Employees data.txt","w")
    limit=int(input("Enter total number of employees data you want to give:"))
    for i in range(limit+1):
                    name=input("Enter the name of the employee: ")
                    DOB=int(input("Enter the date of birth of employee in numbers: "))
                    number=int(input("Enter the contact number of the employee: "))
                    salary=int(input("Enter total income earn by the employ:"))

                    s=name+' '+str(DOB)+' '+str(number)+' '+str(salary)+"\n"
                    f.writelines(s)
                    f.close()
def data_reading():
    zx=open("Employees data.txt")
    print(zx.readlines())
    zx.close()
Employee()
data_reading()

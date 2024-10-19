'''Assignment No.: 12
Title:Write a programme to input the data and create a text file with data of employees .Show the data after reading the file.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
def Data():
    f=open("Employees data.txt","w")
    limit=int(input("Enter total number of employees data you want to give:"))
    for i in range(limit):
                    name=input("Enter the name of the employee: ")
                    date=input("Enter the date of birth in the the format of DD/MM/YYYY")
                    number=int(input("Enter the contact number of the employee: "))
                    salary=int(input("Enter total income earn by the employee:"))
                    s=name+' '+date+' '+str(number)+' '+str(salary)+"\n"
                    f.write(s)
    f.close()
def Dataread():
                li,di=[],{}
                zx=open("Employees data.txt")
                data=zx.read()
                print("Data of all employees")
                fe=data.split()
                for z in fe:
                    print(z,'\n')
                zx.close()
Data()
Dataread()

'''Assignment No.: 15
title:Write a programme to show searching and modification in binary file using random access.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
import pickle,os
def dictionary():
                ch='yes'
                f=open("Emloyees data.dat","wb+",)
                l=[]
                while ch=='yes' or ch=='YES':
                                rollno=int(input("Enter the ID no. of the Employee: "))
                                name=input("Enter the name of the employee: ")
                                marks=int(input("Enter the yearly package of the employee: "))
                                d=[rollno,name,marks]
                                l.append(d)
                                ch=input("Want to give more details (yes/no):")
                                if ch in 'noNONo':
                                                break
                print("Data successfully stored...")
                pickle.dump(l,f)
                f.close()
def search_dictionary():
                f=open("Emloyees data.dat","rb")
                search=pickle.load(f)
                print("data after modification in file...",search)
                found=0
                number=int(input("Enter the ID number of an employee to be searched: "))
                for i in search:
                                if i[0]==number:
                                                print("Record found successfully...")
                                                print(i[0],i[1],i[2])
                                                found=1
                                                print(i[0])
                f.close()
def modify():
                dup=[]
                f=open("Emloyees data.dat","rb+")
                f2=open("Employeedup.dat","wb+")
                search=pickle.load(f)
                print("data before modifying in file...",search)
                found=0
                number=int(input("Enter the ID number of an employee to be modified: "))
                for i in search:
                                if i[0]==number:
                                                print("Record found successfully...")

                                                i[2]=int(input("enter the new salary.."))
                                                found=1
                                                pickle.dump(i,f2)
                                else:
                                                pickle.dump(i,f2)
                                                
                f.close()
                f2.close()
                os.remove("Emloyees data.dat")
                os.rename("employeedup.dat","Emloyees data.dat")
                print("Record modified...in RAM and modified record is saved in file")
dictionary()
search_dictionary()
modify()

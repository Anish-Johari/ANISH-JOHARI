#INSERTING RECORDS IN CSV FILE AND READING IT AND DISPLAYING IT
from csv import *
def csv_writing():
    file=open("data.csv","w")
    write=writer(file)
    for i in range(1,6):
        if i==1:
            roll_no=int(input("ENTER FIRST ROLL NO : "))
            name=input("ENTER FIRST NAME : ")
            marks=input("ENTER THE MARKS OPTAIN BY THE FIRST STUDENT : ")
            DATA=[roll_no,name,marks]
            write.writerow(DATA)
        elif i==2:
            roll_no=int(input("ENTER SECOND ROLL NO : "))
            name=input("ENTER SECOND NAME : ")
            marks=input("ENTER THE MARKS OPTAIN BY THE SECOND STUDENT : ")
            DATA=[roll_no,name,marks]
            write.writerow(DATA)
        elif i==3:
            roll_no=int(input("ENTER THIRD ROLL NO : "))
            name=input("ENTER THIRD NAME : ")
            marks=input("ENTER THE MARKS OPTAIN BY THE THIRD STUDENT : ")
            DATA=[roll_no,name,marks]
            write.writerow(DATA)
        if i==4:
            roll_no=int(input("ENTER FOURTH ROLL NO : "))
            name=input("ENTER FOURTH NAME : ")
            marks=input("ENTER THE MARKS OPTAIN BY THE FOURTH STUDENT : ")
            DATA=[roll_no,name,marks]
            write.writerow(DATA)
        if i==5:
            roll_no=int(input("ENTER FIFTH ROLL NO : "))
            name=input("ENTER FIFTH NAME : ")
            marks=input("ENTER THE MARKS OPTAIN BY THE FIFTH STUDENT : ")
            DATA=[roll_no,name,marks]
            write.writerow(DATA)
    file.close()
def csv_reading():
    file=open("data.csv","r")
    read=reader(file)
    for i in read:
        print(i)
csv_writing()
csv_reading()

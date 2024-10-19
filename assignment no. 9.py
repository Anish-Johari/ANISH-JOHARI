'''Assignment No.: 9
title:Write a programme to create and read the text file and display the content.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
def Write(): 
                f=open("Students data.txt","w")
                tr="Roll number  Name  percentage""\n"
                f.write(tr)
                d=int(input("how many students data you want to give: "))
                for i in range(1,d+1):
                                a=int(input("Enter the roll number of the student: "))
                                b=input("Enter the name of the student:")
                                z=int(input("Enter total percentage of a student obtained in examination: "))
                                za=str(a)+' '+b+' '+str(z)+" "+"\n"
                                f.writelines(za)
                f.close()
def Read():
                f=open("Students data.txt")
                re=f.readlines()
                for i in re:
                                print(i)
Write()
Read()

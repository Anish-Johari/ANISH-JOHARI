'''Assignment No. 21
Title: write a programme to make the pattern using loop
Date:21/11/2022
Developed by: Anish Johari
_______________________________________'''
c='y'
while c=='y' or c=='Y':
                a=int(input("enter the no. of rows"))
                for i in range(1,a):
                    print("*"*i)
                c=input('Do you want to continue: ')

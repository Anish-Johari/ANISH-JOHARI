'''Assignment No. 22
Title: write a programme to make the pattern using loop
Date:21/11/2022
Developed by: Anish Johari
_______________________________________'''
c='y'
while c=='y' or c=='Y':
    a=int(input("enter a number for creating a right triangle:  "))
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(j ,end=' ')
        print()
    c=input("Do you want to continue(then press y\Y): ")

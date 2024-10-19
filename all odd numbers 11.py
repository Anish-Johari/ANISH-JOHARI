'''Assignment No. 11
Title: write a programme to display all odd numbers given by user
Date:03/11/2022
Developed by: Anish Johari
_______________________________________'''
l=int(input("enter lowerlimit:"))
n=int(input("enter upperlimit:"))
for i in range(l,n+1):
    if i%2==1:
        print(i,end=' ')

'''Assignment No. 23
Title: write a programme to make a hollow triangle pattern using loop
Date:24/11/2022
Developed by: Anish Johari
_______________________________________'''
s=0
n=int(input('Enter the number of lines: '))
for i in range (1,n):
                for j in range(i,n):
                                print(" ",end=" ")
                while s!=(2*i-1):
                                if s==0 or s==(2*i-2):
                                                print("*",end=" ")
                                else:
                                                print(" ",end=" ")
                                s=s+1
                s=0
                print()
for i in range(0,(2*n)-1):
                print("*",end=" ")

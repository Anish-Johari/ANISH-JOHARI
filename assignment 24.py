'''Assignment No. 24
Title: write a programme ti reverse a string without slicing.
Date:01/12/2022
Developed by: Anish Johari
_______________________________________'''
n=input("Enter a string to be reversed: ")
for i in range(len(n)-1,-1,-1):
                print(n[i],end='')

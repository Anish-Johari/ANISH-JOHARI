'''Assignment No. 19
Title: write a programme to display sum of digits of a integer given as input
Date:21/11/2022
Developed by: Anish Johari
_______________________________________'''
n=int(input("enter more then one digit number for getting sum of digits: "))
s=0
while n>0:
    s=s+n%10
    n=n//10
print(s)

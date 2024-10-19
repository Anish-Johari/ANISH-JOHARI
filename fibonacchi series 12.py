'''Assignment No. 12
Title: write a programme to display fibonance series upto n terms
Date:03/11/2022
Developed by: Anish Johari
_______________________________________'''
a=1
b=1
c=int(input("Enter a range of fibonachi series:"))
print(a)
print(b)
for i in range (1,c+1):
    c=a+b
    print(c)
    a=b
    b=c
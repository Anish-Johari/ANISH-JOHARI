''' Assignment No:07
Title: write a programme to find a greatest of three number
Date:25/08/2022
Developed by: Anish Johari'''
a=int(input("enter a value"))
b=int(input("enter second value"))
c=int(input("enter third value"))
if a>b:
    print(a,"is the greatest")
else:
    if b>c:
        print(b,"is the greatest")
    else:
        print(c,"is the greatest")

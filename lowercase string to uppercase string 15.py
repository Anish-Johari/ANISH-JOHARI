'''Assignment No. 15
Title: write a programme for changing lowercase string into uppercase string
Date:10/11/2022
Developed by: Anish Johari
_______________________________________'''
a=input("enter a string in lowercase:  ")
for i in range(0,len(a)):
    b=ord(a[i])
    c=b-32
    d=chr(c)
    print(d,end=' ')

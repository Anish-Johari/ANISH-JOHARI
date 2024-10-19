'''Assignment No.: 02
Title: Write a programme that display n terms of fibonachi series.
Date:06/04/2023
Developed by: Anish Johari
_______________________________________'''
def series():
    while True:
        n=int(input("Enter total number of terms for fibonachi series:"))
        a=-1
        b=1
        for i in range(1,n+1):
            c=a+b
            print(c,end=' ')
            a=b
            b=c
        ch=input("\nPress y/Y to continue giving numbers otherwise press n/N: ")
        if ch in 'nN':
            break
series()

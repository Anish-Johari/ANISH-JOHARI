'''Assignment No. 14
Title: write a programme to calculate sum of series 1/2+1/4+......n
Date:07/11/2022
Developed by: Anish Johari
_______________________________________'''
n=int(input("enter a limit for for this series: "))
a=2
b=0
for i in range(1,n+1):
    c=1/a
    b=c+b
    a=a+2
    print(b,end='  ')
            

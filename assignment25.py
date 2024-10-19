'''Assignment No. 25
Title: write a programme to input a string and one character.Find frequency of character in string.
Date:01/12/2022
Developed by: Anish Johari
_______________________________________'''
d='y'
while d=='y' or d=='Y':
    a=0
    s=input('Enter a string: ')
    c=input('enter a character to be find the frequency: ')
    for i in range(0,len(c)):
        if i in s:
            a=a+1
            print(a,end=' ')
    d=input('Do you want to continue: ')

'''Assignment No. 25
Title: write a programme to input a string and one character . Find frequency of character in string.
Date:01/12/2022
Developed by: Anish Johari
_______________________________________'''
p='y'
while p=='y' or p=='Y':
                 s=input("Enter a string: ")
                 c=input("Enter a alphabet for finding frequency in string: ")
                 p=list(s)
                 s=p.count(c)
                 print(s)
                 p=input('Do you want to continue: ')

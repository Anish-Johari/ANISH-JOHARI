'''Assignment No. 26
Title: write a programme to input a string and find number of vowals in it
Date:01/12/2022
Developed by: Anish Johari
_______________________________________'''
c='y'
while c=='y' or c=='Y':
                A=0
                n=input("Enter a string for finding no. of vowals in it: ")
                for i in range(0,len(n)):
                                if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u' or n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U':
                                                A=A+1
                print(A)
                c=input('Do you want to continue: ')

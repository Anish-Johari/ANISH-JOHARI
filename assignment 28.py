'''Assignment No. 28
Title: write a programme to input a string ond perform the following operation
                1. Display all the wards begains with capital alphabet
                2. Display all wards that begains and end with vowel
                3. Display all wards that end with vowel and have 5 character in it.
Date:15/12/2022
Developed by: Anish Johari
_______________________________________'''
c='y'
while c=='y' or c=='Y':
                n=input('Enter a string for finding capital alphabet: ')
                n.split()
                for i in n:
                                if i[0].isupper():
                                                print(i)
                c=input('Do you want to check more wards: ')

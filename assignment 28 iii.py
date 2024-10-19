'''Assignment No. 28
Title: write a programme to input a string ond perform the following operation
                3. Display all wards that ende with vowal and have 5 character in it.
Date:15/12/2022
Developed by: Anish Johari
_______________________________________'''
n=input('enter a senterce for finding vowal and 5 alphabet ward: ')
l=n.split()
for i in l:
                if len(i)==5 and i[-1]=='aeiouAEIOU':
                                print(i,end=' ')
                                

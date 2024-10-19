'''Assignment No. 28
Title: write a programme to input a string ond perform the following operation
                2. Display all wards that begains and end with vowel
Date:15/12/2022
Developed by: Anish Johari
_______________________________________'''
n=input('Enter a sentence for finding first and last vowel alphabet: ')
n.split()
for i in n:
                if i[0]in 'aeiouAEIOU' and i[-1]in 'aeiouAEIOU':
                                print(i,end=' ')

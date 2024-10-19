'''Assignment No.: 06
Title: Write a function that accept a string and returns total capital alphabet in it.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
def string(a):
                z=0
                for i in a:
                                if i.isupper():
                                                z=z+1
                return z
if __name__=="__main__":
                c='y'
                while c=='y' or c=='Y':
                                a=input("Enter a sentence for checking total number of capital alphabet:")
                                print("The total capital alphabet present in the given sentence is:  ",string(a))
                                c=input("Press n/N to exit else press  y to continue")
                                if c in "nN":
                                                break


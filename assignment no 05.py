'''Assignment No.: 05
Title: Create a function that returns a list of n multiples of a number m.
Date:13/04/2023
Developed by: Anish Johari
_______________________________________'''
ch='y'
while ch=='y' or ch=='Y':
    def multiples(a,b):
        l=[]
        for i in range(1,a+1):
            s=b*i
            l.append(s)
        return l 
    if __name__=="__main__":    
        b=int(input("Enter a number for which you want multiples:"))
        a=int(input("Enter a total number of times a number gets multiplied: "))
        print("A list of multiples of a number which gets multiplied is : ",multiples(a,b))

    ch=input("Press y/Y to continue giving numbers otherwise press n/N: ")
    if ch in 'nN':
        break

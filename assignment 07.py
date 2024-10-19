'''Assignment No.: 07
Title: Create a function that takes 2 integers argument and return their HCF.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
ch='y'
while ch=='y' or ch=='Y':
    def HCF(a,b):
        if a>b:
            smaller=b
        else:
            smaller=a
        for i in range(1,smaller+1):
            if (a%i)==0 and (b%i)==0:
                hcf=i
        return hcf
    if __name__=="__main__":
        a=int(input("Enter first number for calculation of hcf: "))
        b=int(input("Enter second number for calculation of hcf: "))
        print("The hcf of given two numbers is : ",HCF(a,b))
    ch=input("Press y/Y to continue giving numbers for HCF otherwise pressn/N: ")
    if ch in 'nN':
        break

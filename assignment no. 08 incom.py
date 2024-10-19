'''Assignment No.: 08
Title: Create a function with inner function.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
print("Enter the four integer values to get the product of the sum of the first two and next two values for example for the values like 2,3,6,8 the result will be(2+3)*(6+8)")
ch='y'
while ch=='y' or ch=='Y':
                def sum(a,b,f,g):
                    d=a+b
                    e=f+g
                    return multiply(d,e)
                def multiply(d,e):
                    return d*e
                if __name__=="__main__":
                                a=int(input("Enter a number for mathematical operation:"))
                                b=int(input("Enter a number for mathematical operation:"))
                                f=int(input("Enter a number for mathematical operation:"))
                                g=int(input("Enter a number for mathematical operation:"))
                                print("The value obtain by adding and multiplying the given numbers is",sum(a,b,f,g))
                ch=input("Press y/Y for giving more values otherwise press n/N: ")
                if ch in "nN":
                                break

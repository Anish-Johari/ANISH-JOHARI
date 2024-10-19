'''Assignment No.: 04
Title: Create a function to calculate simple interest with 2 years time as default value.
Date:14/04/2023
Developed by: Anish Johari
_______________________________________'''
while True:
    def interest(p,r,t=2):
        return (p*r*t)/100
    if __name__=="__main__":
        a=int(input("Enter a principal amount for finding interest amount: "))
        b=eval(input("Enter the rate of interest for finding interest amount:"))
        c=int(input("Enter the time period for finding interest amount:"))
        print("The total simple interest amount is ",interest(a,b),"rupees")
    ch=input("Press y/Y to continue the programme otherwise press n/N: ")
    if ch in 'nN':
        break

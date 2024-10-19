'''Assignment No.: 03
Title: Create a function for temperature conversion.
Date:06/04/2023
Developed by: Anish Johari
_______________________________________'''
while True:
                def temp(b,f):
                    if b==1:
                        return ((f-32)*5//9)
                    else:
                        return ((f*9//5)+32)
                if __name__=="__main__":
                    print("1. Convert degree fahrenheit to degree elcious")
                    print("2. Convert degree celcious to degree fahrenheit")
                    b=int(input("Enter your choice:"))
                    f=int(input("Enter a temperature value: "))
                    Z=(temp(b,f))
                    print("The converted value of given temperature is : ", Z , " degree Celsius//Fahreneit")

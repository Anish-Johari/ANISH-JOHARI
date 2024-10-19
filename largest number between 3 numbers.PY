#4.	Develop a Python program to find the largest among three numbers using conditional statements.

num1=int(input(" ENTER FIRST NUMBER: "))
num2=int(input(" ENTER SECOND NUMBER: "))
num3=int(input(" ENTER THIRD NUMBER: "))

if num1>num2 and  num1> num3:
    print("THE GREATEST NUMBER IS : ",num1)
elif num2>num1 and num2>num3:
    print("THE GREATEST NUMBER IS : ",num2)
else:
    print("THE GREATEST NUMBER IS : ",num3)
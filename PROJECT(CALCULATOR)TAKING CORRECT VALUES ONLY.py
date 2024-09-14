print("**********CALCULATOR**********")
print("1. ADDITION(A/a)\n2. SUBTRACTION(S/s) \n3. MULTIPLICATION(M/m) \n4. DIVISION(D/d)\n5. EXIT FROM CALCULATOR(E/e)\n")
print("******************************")
while True:
    choice=input("PROVIDE US YOUR CHOICE BY GIVING ALPHABETS WRITTEN BESIDES THEM : ")
    if choice in ('A','a','S','s','D','d','M','m','E','e'):
        break
    else:
        print("\nGIVEN DATA IS INVALID PLEASE PROVIDE US THE CORRECT DATA FROM ABOVE...\n")
        continue
if choice=="A" or choice=="a":
    num1=int(input("ENTER FIRST VALUE : "))
    num2=int(input("ENTER SECOND VALUE : "))
    add=num1+num2
    print("THE ADDITION OF GIVEN VALUES ARE ",add)
elif choice=="S" or choice=="s":
    num1=int(input("ENTER FIRST VALUE : "))
    num2=int(input("ENTER SECOND VALUE : "))
    sub=num1-num2
    print("THE SUBTRACTION OF GIVEN VALUES ARE ",sub)
elif choice=="M" or choice=="m":
    num1=int(input("ENTER FIRST VALUE : "))
    num2=int(input("ENTER SECOND VALUE : "))
    mul=num1*num2
    print("THE MULTIPLICATION OF GIVEN VALUES ARE ",mul)
elif choice=="D" or choice=="d":
    num1=int(input("ENTER FIRST VALUE : "))
    num2=int(input("ENTER SECOND VALUE : "))
    divide=num1/num2
    print("THE DIVISION OF GIVEN VALUES ARE ",divide)
elif choice=="E" or choice=="e":
    exit()
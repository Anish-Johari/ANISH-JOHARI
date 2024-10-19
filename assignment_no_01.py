'''Assignment No.: 01
Title: Write a programme to check whether a given number is prime or not.
Date:06/04/2023
Developed by: Anish Johari
_______________________________________'''
def prime():
                while True:
                                a=int(input("enter a number for checking whether it is prime or not: "))
                                if a>1:
                                    for i in range(2,a):
                                        if a%i==0:
                                            print(a,'is not a prime number')
                                            break
                                    else:
                                            print(a,'is a prime number')
                                else:
                                    print(a,'is not a prime number')
                                c=input("Press y/Y to continue otherwise press n/N: ")
                                if c in 'nN':
                                                break
prime()    


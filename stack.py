'''Assignment No.: 26
Title: Write a programme of stack using list.
Date:05/10/2023
Developed by: Anish Johari
_______________________________________'''
stack=[]
ch='y'
def push(n):
                stack.append(n)
def pop():
                if not len(stack)==0:
                                show=stack[-1]
                                del stack[-1]
                return show
def display():
                if not len(stack)==0:
                                print("The satck is : ")
                                for i in range(len(stack)-1,-1,-1):
                                                print(stack[i])
                else:
                                print("The stack is empty..")
if __name__=="__main__":
                while ch=="y" or ch=="Y":
                                print("===MENU FOR SATCK OPERATIONS===\n  1. Enter an element.\n  2. Remove an element.")
                                choice=int(input("Enter your choice : "))
                                if choice==1:
                                                d=int(input("Enter the element : "))
                                                push(d)
                                                display()
                                elif choice==2:
                                                print("The element",pop(),"popped from the stack.")
                                                display()
                                ch=input("Do you want to continue : ")
                                if ch=='n' or ch=='N':
                                                break

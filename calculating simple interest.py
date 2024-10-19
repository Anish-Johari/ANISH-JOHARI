'''Assignment No. 10
Title: write a programme to calculate simple interest
Date:08/09/2022
Developed by: Anish Johari
_______________________________________'''
p=int(input("enter a amount"))
t=int(input("enter time period in years"))
if p<5000:
    print("the simple interest is",p*3*t/100)
else:
    if p>=5000:
        print("the simple interest is",p*6*t/100)
    else:
        if p<=50000:
            print("the simple interest is",p*6*t/100)
        else:
            if p>50000:
                 print("the simple interest is",p*8*t/100)
    
             

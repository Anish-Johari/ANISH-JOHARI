#W.A.P. TO ADDITION THE EVEN AND ODD NUMBERS FROM 1 TO 20
even=1
odd=1
for i in range(1,21,1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print("THE MULTIPLIED VALUES OF EVEN NUMBERS ARE ", even)
print("THE MULTIPLIED VALUES OF ODD NUMBERS ARE ", odd)


#ADDING THE SUM OF EVEN NUMBERS AND ODD NUMBERS 
even=0
odd=0
#BY USING 'FOR' LOOP WE WILL ADD 'EVEN' AND 'ODD' NUMBERS
for i in range(1,31):
    if i%2==0:
        #HERE ONLY THE EVEN NUMBERS WILL BE ADDED
        even+=i
    else:
        #HERE ONLY THE ODD NUMBERS WILL BE ADDED
        odd+=i
print("THE ADDED VALUE OF 'EVEN' NUMBERS IS : ",even,"\n")
print("THE ADDED VALUE OF 'ODD' NUMBERS IS : ",odd)
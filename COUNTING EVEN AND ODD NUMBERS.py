count_even=0
count_odd=0
a=int(input("PROVIDE US THE INITIAL VALUE OF SERIES : "))
b=int(input("PROVIDE US THE INITIAL VALUE OF SERIES : "))

for i in range(a,b+1):
    if i %2==0:
        count_even+=1
    else:
        count_odd+=1
print("COUNT OF EVEN NUMBERS : ",count_even)
print("COUNT OF ODD NUMBERS : ",count_odd)

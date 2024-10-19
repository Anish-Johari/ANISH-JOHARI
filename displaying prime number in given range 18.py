#WRITING A PROGRAMME TO DISPLAY ALL PRIME NUMBERS GIVEN IN A RANGE

A=int(input("ENTER A LOWER LIMIT FOR PRIME NUMBERS"))

B=int(input("ENTER A UPPER LIMIT FOR PRIME NUMBERS"))

for i in range(A,B+1):

    if i>1:

        for y in range(2,i):

            if i%y==0:

                break

        else:
            print(i,end=' ')









n=int(input("ENTER A DIGIT HAVING MORE THEN ONE VALUES : "))
while(n !=0):
    last_number=n%10
    print(last_number,end="")
    n=n//10

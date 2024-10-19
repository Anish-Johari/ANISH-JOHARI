'''Assignment No. 30
Title: write a programme to create a dictionary of 5 students for roll no. ,name, and marks and display the marks of topper.
Date:24/11/2022
Developed by: Anish Johari
_______________________________________'''
D={}
for i in range(0,5):
    r=int(input("Enter a roll no. of student: "))
    n=input("Enter a name of student:")
    m=int(input("Enter marks of student: "))
    D[r]=(n,m)
print(D)
hname=max(D, key = D.get)
hmarks=max(D.values())
print("students with highest marks is ",hname,"scored ",hmarks)
'''Assignment No. 16
Title: write a programme to calculate n terms of the series 3,8,15,24,35,..........n
Date:10/11/2022
Developed by: Anish Johari
_______________________________________'''
n=int(input("enter last number for getting total sum:  "))
for i in range(2,n+1):
      a=((i**2)-1)
      print(a,end=' ')

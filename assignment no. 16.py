'''Assignment No.: 17
title:Read the CSV file created in programme 16 and display the entire data and perform the search operation.
Date:17/04/2023
Developed by: Anish Johari
_______________________________________'''
import csv
def CSV_FILE_READING():
    with open('Employees_data_in_CSV.csv','r') as sum:
        reades=csv.reader(sum)
        for i in reades :
            print(i)
def SEARCHING_CSV_FILE():
    with open('Employees_data_in_CSV.csv','r') as sum:
        reades=csv.reader(sum)
        search=input("Enter the identity number of an employee to be searched in CSV file: ")
        next(reades)
        for j in reades :
            if j[0]==search:
                print("Data found successfully...")
                for k in j:
                    print(k,end="  ")
                break
        else:
            print("Data does\'t exist... ")
    sum.close()
CSV_FILE_READING()
SEARCHING_CSV_FILE()

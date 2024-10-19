'''Assignment No.: 18
Title: Write a programme to show exception handling in python.
Date:18/05/2023
Developed by: Anish Johari
_______________________________________'''
def writing(n):
                f=open("Text_file.txt","w")
                f.write(n)
                f.close()
def reading():
                try:
                                words=[]
                                count=0
                                f=open("Text_file.txt","r")
                                read=f.read()
                                sp=read.split()
                                for i in sp:
                                                if i[0] in "aeiouAEIOU":
                                                                count=count+1
                                                                words.append(i)
                except:
                    f.close()
                finally:
                    print("The total number of words that starts with vowel are ","\'",count,"\'","and the words are", words)
if __name__=="__main__":
                n=input("Enter the sentence to be stored : ")
                writing(n)
                reading()

while True:
                print('         MENU\n1.  CREATE STUDENT DATA.\n2.  REMOVE A STUDENT.\n3.  UPDATE STUDENT DETAILS.\n4.  DISPLAY STUDENTS DETAILS.')
                n=int(input("Enter your choice: "))
                if n==1:
                                R=[]
                                M=[]
                                s=int(input("enter total students"))
                                for i in range(1,s+1):
                                                r=int(input("enter roll number"))
                                                n=input("Enter name")
                                                m=int(input("Enter percentage"))
                                                R=[r,n,m]
                                                M.append(R)
                                print(M)
                elif n==2:
                                P=int(input("enter roll no. of student for deleting details: "))
                                for j in M:
                                                if j[0]==P:
                                                                M.remove(j)
                elif n==3:
                              update=int(input("enter a roll number of student for updation: "))
                              for k in M:
                                              if k[0]==update:
                                                              k[0]=int(input("Enter a new roll number: "))
                                                              k[1]=input("Enter a new name: ")
                                                              k[2]=int(input("Enter a new percentage: "))
                              print(M)
                elif n==4:
                                z=str(input("Press f for full list otherwise press any key: "))
                                if z=='f':
                                                print(M)
                                else:
                                                particular=int(input("Enter roll no. of a student: "))
                                                for L in M:
                                                                if L[0]==particular:
                                                                                print(L)
                else:
                    print("                             invalid choice. ")
               
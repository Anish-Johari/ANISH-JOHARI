""" Write a programme that accept a character from user and give the following message.
You enter a Upper case character.
You enter a Lower case character.
You enter a digit character.
You enter a special character."""
c = 'y'
while c == 'y' or c == 'Y':
    a = input("enter any Character: ")
    if a =='a':
        print("You entered a Lower case character.")
    elif a =='A':
        print("You entered a upper case character.")
    elif a =='1':
        print("You entered a Digit.")
    elif a=='\\' or a =='*' or a=="#" or a=='\'':
        print("You entered a special character.")
    c=input("Do you want to continue:")
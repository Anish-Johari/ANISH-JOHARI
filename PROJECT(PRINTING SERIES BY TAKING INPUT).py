# DISPLAYING A SERIES BY TAKING INITIAL,FINAL,UPDATION VALUES FROM USER AND ALSO DISPLAYING TYPE LIKE HORIZONTAL OR VERTICAL ALSO IN REVERSE OR FOREWARD ORDER.

# Take inputs from the user
initial = int(input("PROVIDE US THE INITIAL VALUE OF A SERIES: "))
final = int(input("PROVIDE US THE FINAL VALUE OF A SERIES: "))
updation = int(input("PROVIDE US THE updation VALUE OF A SERIES BY WHICH SERIES MUST GET UPDATED EACH TIME: "))
horizontal = input("HOW YOU WANT THE SERIES TO GET DISPLAYED IN HORIZONTAL(type H/h) or vertical(type V/v): ")
order = input("HOW YOU WANT THE SERIES TO GET DISPLAYED IN REVERSE ORDER(type R/r) OR IN FOREWARD ORDER(type F/f): ")

# Validate the updation value
if updation <= 0:
    print("Updation value must be greater than 0.")
else:
    # Horizontal display
    if horizontal== 'h':
        if order == 'r':
            for i in range(final, initial - 1, -updation):
                print(i, end=" ")
        elif order == 'f':
            for i in range(initial, final + 1, updation):
                print(i, end=" ")
        elif horizontal== 'H':
            if order == 'R':
                for i in range(final, initial - 1, -updation):
                    print(i, end=" ")
            elif order == 'F':
                for i in range(initial, final + 1, updation):
                    print(i, end=" ")
        else:
            print("Invalid order input. Please type 'R/r' for reverse or 'F/f' for forward.")

     # Vertical display
    elif horizontal == 'v':
        if order == 'r':
            for i in range(final, initial - 1, -updation):
                print(i)
        elif horizontal == 'V':
            if order == 'R':
                for i in range(final, initial - 1, -updation):
                    print(i)        
            elif order== 'F':
                for i in range(initial, final + 1, updation):
                    print(i)
            elif order== 'f':
                for i in range(initial, final + 1, updation):
                    print(i)
        else:
            print("Invalid order input. Please type 'R/r' for reverse or 'F/f' for forward.")

    else:
        print("Invalid horizontal input. Please type 'H/h' for horizontal or 'V/v' for vertical.")
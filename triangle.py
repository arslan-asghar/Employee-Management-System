
h = int(input("enter hypotenuse "))

row = 1
while row <= h:
    col = 1
    while col <= row <= h:

        if col == 1 and row == 1:
            print("*", end=" ")
            col = col + 1
            row = row + 1
            break
        elif col == 1 and row < h:
            print("*", end=" ")
            col = col + 1
        elif row == col and 1 < row < h:
            print("*", end="")
            row = row + 1
            break
        elif row == h:
            print("*", end=" ")

            if col == h:
                row = row + 1
            col = col + 1
        else:
            print(end="  ")
            col = col + 1
    print("\n")
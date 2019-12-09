def input_number(message):
    while True:
        try:
            val = int(input(message))

        except ValueError:
            print("value must be an integer value")
            continue
        else:
            return val
            break


Choice = input_number("enter Desired Value")
k = Choice
i = 1
while i <= Choice:

    z = 1
    if i == 1 or i == Choice:
        while z <= k:
            print("*", end="  ")
            if z == k:
                print("\n")
            z = z + 1
    else:
        z = 1
        while z <= k:
            if z == 1:
                print("*", end="  ")
            elif z == k:
                print("*\n")
            else:
                print(" ", end="  ")

            z = z + 1
    i = i + 1
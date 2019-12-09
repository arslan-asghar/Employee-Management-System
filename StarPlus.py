i = 0
p = int(input("enter your desiger value"))
j = p-1
if (j % 2) == 0:
    center = j/2

else:
    center = (j / 2)-0.5
for row in range(p):
    for col in range(p):
        if row == i and col == j:
            print("*", end=" ")
            i = i + 1
            j = j - 1
        elif row == center:
            for cen in range(p):
                print("*", end=" ")
            i = i + 1
            j = j - 1
            break
        elif row == col:
            print("*", end=" ")
        else:
            if col == center:
                print("*", end=" ")
            else:
                print(end="  ")
    print("\n")
# i = 0
# j = 4
# center = j/2
# for row in range(5):
#     for col in range(5):
#         if row == i and col == j:
#             print("*", end="")
#             i = i + 1
#             j = j - 1
#         elif row == col:
#             print("*", end="")
#         else:
#             print(end=" ")
#     print("\n")

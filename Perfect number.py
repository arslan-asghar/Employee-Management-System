import math


def integer_number(msg):
    while True:
        try:
            v = int(input(msg))
        except ValueError:
            print("must be integer value")
            continue
        else:
            return v
            break


print("-------------------------------------------------\n           ُPerfect Numbers")
print("-------------------------------------------------")

va = integer_number("Enter your value : ")
list_of_perfect_numbers = [1]

perfect = (va/2)+1

if perfect % 2 != 0 and perfect % 3 != 0:
    perfect = int(perfect - 0.5)
else:
    perfect = int(perfect)


perfect_number = 1
for i in range(perfect):
    if i > 1:
        if va % i == 0:
            perfect_number = perfect_number + i
            list_of_perfect_numbers.append(i)

if perfect_number == va:

    for i in list_of_perfect_numbers:
        if i != perfect_number/2:
            print(i, end=" + ")
        else:
            print(i, end=" = ")
    print(perfect_number)
    print("YES", va, "is a perfect number")
else:

    print("NO", va, "is not a perfect number")
print("-------------------------------------------------")



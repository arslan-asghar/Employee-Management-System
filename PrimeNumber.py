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


print("-------------------------------------------------\n           Prime numbers string")
print("-------------------------------------------------")
print("Find the prime numbers\n1 - Full number of string till your input value\n2 - For individual number")
choice = integer_number("Enter your choice : ")

if choice == 1:
    va = integer_number("Enter your value : ")
    print("-------------------------------------------------\n           String of PRIME numbers till ", va)
    print("-------------------------------------------------")
    for i in range(va):
        if i%2 != 0 and i%3 != 0 and i > 3:
            print(i, end=" ")
        elif i < 3:
            print(i, end=" ")
        else:
            pass
    print("-------------------------------------------------")

elif choice == 2:
    i = integer_number("Enter your value : ")

    print("-------------------------------------------------\n           Is", i, "a prime number? ")
    print("-------------------------------------------------")
    if i % 2 != 0 and i % 3 != 0 and i > 3:
        print(i, end=" Is a prime number")
    else:
        print(i, end=" Is NOT a prime number")
    print("\n-------------------------------------------------")
else:
    print("you chosed rong value")


def input_number(message):
    while True:
        try:
            val = int(input(message))
        except ValueError:
            print("Value should be an integer", end=" Again ")
            continue
        else:
            return val
            break


Choice = input_number("Enter your desier value")
i = 1
L = Choice
c = Choice
f= Choice
o = Choice
while i <= Choice:
    j = 1
    while j < i:
        print(end="  ")
        j = j+1
    print("*", end=" ")
    p = 1
    k = L
    while k >= p:
        print(end="  ")
        k = k - 1
    print("*", end=" ")
    L = L - 1

    a = 1
    b = c
    while b >= a:
        print(end="  ")
        b = b - 1
    print("*", end=" ")
    c = c - 1
    i = i + 1
    print("\n")
k = 1
if Choice > 2:
    while k <= Choice:
        print(end="  ")
        k = k + 1
    print("*  *\n")
hr = Choice * 2
i = 1

while i <= hr:
    print("*", end="  ")
    i = i + 1

print("\n")
k = 1
while k <= Choice:
    print(end="  ")
    k = k + 1
print("*  *\n")


g = Choice
i = 1
while i <= g:
    k = g - i
    while k<g-1:
        print(end="  ")
        k = k + 1
    print("*")
    i = i + 1


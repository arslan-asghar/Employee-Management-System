palindrome = input("enter your value")
g = len(palindrome)
length = g
i = 0
g = g/2
if g % 2 != 0 and g % 3 != 0:
    g = int(g + 0.5)
else:
    g = int(g)

true = 1
while i < g and true == 1:
    while length >= g:
        if palindrome[i] == palindrome[length-1]:
            i = i + 1
            length = length - 1
            true = 1
            continue
        else:

            true = 0
            break
if true == 1:
    print(" '", palindrome, "' is a palindrome")
else:
    print(" '", palindrome, "' is not a palindrome")
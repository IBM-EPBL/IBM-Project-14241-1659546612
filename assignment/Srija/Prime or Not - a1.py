import math
a = int(input("Enter the number to be checked : "))
flag = 1
if a > 2:
    for i in range(2, math.ceil(math.sqrt(a))+1):
        if (a % i) == 0:
            print(a, " is not a PRIME number")
            flag = 0
            break
    if flag == 1:
        print(a, " is a PRIME number")
elif a > 1:
    print(a, " is a PRIME number")
else:
    print(a, " is neither PRIME nor COMPOSITE")

import math
a = int(input("Enter the UPPER limit value : "))
if a == 0 or a == 1:
    print(a , " is neither PRIME nor COMPOSITE")
else:
    print("List of PRIME numbers : ")
for i in range(2,a+1):
    if i > 2:
        flag = 1
        for j in range(2, math.ceil(math.sqrt(i))+1):
            if (i % j) == 0:
                flag = 0
                break
        if flag == 1:
            print(i, end = " ");
    elif i > 1:
        print(i, end = " ")

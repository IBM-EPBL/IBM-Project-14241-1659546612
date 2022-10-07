 a = 0
b = 1
n = int(input("Enter the number of elements of fibonacci series : "))
print("List of fibonacci series are : ")
print(a, end = " ")
print(b, end = " ")
for i in range(0,n-2):
    fib = a + b
    print(fib, end = " ")
    a = b
    b = fib

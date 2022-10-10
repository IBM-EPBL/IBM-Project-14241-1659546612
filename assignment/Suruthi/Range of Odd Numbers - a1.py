m = int(input("Enter the LOWER limit value : "))
n = int(input("Enter the UPPER limit value : "))
if((m==n and m%2==0) or m>n):
    print("No ODD numbers found")
else:
    print("The list of ODD number(s) are: ")
    while m < n+1:
        if(m%2)!=0:
            print(m, end=" ")
        m = m + 1

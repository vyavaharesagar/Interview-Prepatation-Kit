n=5
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for i in range(0,i+1):
        print("*",end=" ")
    print()

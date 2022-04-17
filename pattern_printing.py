'''

* 

* *

* * *

* * * *

* * * * *

'''

   
def pyramid(num):
    for i in range(num):
        for j in range(i+1):
            print(str(i), end=" ")
        print("\n")

# pyramid(5)

def alphabates(num):
    ascii_value = 65
    for i in range(num):
        for j in range(i+1):
            alphabate = chr(ascii_value)
            print(alphabate, end="")
        print("\n")
        ascii_value+=1

# alphabates(5)

def reverse_pyramid(num):
    for i in range(num,-1,-1):
        for j in range(0,i):
            print(j,end=" ")
        print("\n")

# reverse_pyramid(5)

def real_pyramid(rows):
    k = 0
    for i in range(1, rows+1):
        for space in range(1, (rows-i)+1):
            print(end="  ")
        while k!=(2*i-1):
            print("* ", end="")
            k += 1
        k = 0
        print()
        
       


print(real_pyramid(11))
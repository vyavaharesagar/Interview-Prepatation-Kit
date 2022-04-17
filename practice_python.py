# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def prime_numbers(lower,upper):
    for num in range(lower, upper):
        if num>1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
                
# prime_numbers(1,100)

def factorial(num):
    fact = 1
    for i in range(1,num):
        fact += fact * i 
    print(fact)
    
# factorial(5)

def fibonacci_series(num):
    a = 0
    b = 1
    for i in range(num):
        print(a)
        temp = a + b
        b = a
        a = temp
        
# fibonacci_series(9)

def armstrong_number(lower,upper):
    for i in range(lower,upper):
        numbers = list(str(i))
        sum = 0
        for j in range(len(numbers)):
            sum += pow(int(numbers[j]),len(numbers))
        if i == sum:
            print(i)
            
            
# armstrong_number(1,5000)

def is_armstrong_number_or_not(num):
    numbers = list(str(num))
    sum = 0
    for i in range(len(numbers))
        sum += pow(int(numbers[j]),len(numbers))
    if i == sum:
        print("Given number is an armstrong number")
    else:
        print("Given number is not an armstrong number")
        
is_armstrong_number_or_not(1634)


def power(number, exponential):
    return number**exponential

def is_armstrong_number_or_not(num):
    numbers = list(str(num))
    sum = 0
    for i in range(len(numbers)):
        sum += power(int(numbers[i]),len(numbers))
    if num == sum:
        print("Given number is an armstrong number")
    else:
        print("Given number is not an armstrong number")
        
is_armstrong_number_or_not(1634)
# print(power(3,3))
# print the prime numbers bet 1 to 100

def prime_number(lower, upper):
    for num in range(lower, upper+1):
        if num>1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num)

prime_number(0,100)
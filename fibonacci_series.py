def fibonacci_series(num):
    a = 0
    b = 1
    for i in range(num):
        print(a)
        temp = a+b
        a = b
        b = temp

fibonacci_series(9)
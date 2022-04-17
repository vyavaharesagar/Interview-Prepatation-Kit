def armstrong_number(lower,upper):
    for i in range(lower,upper):
        numbers = list(str(i))
        sum = 0
        for j in range(len(numbers)):
            sum += pow(int(numbers[j]),len(numbers))
        if i == sum:
            print(i)
            
            
armstrong_number(1,5000)
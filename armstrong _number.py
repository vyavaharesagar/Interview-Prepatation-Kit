# Write a python code to check the number is armstrong number or not

def is_armstrog_number(num):
    number = list(str(num))
    length = len(number)
    sum = 0
    for i in range(length):
        sum += pow(int(number[i]),length)
    if sum == num:
        return "armstrong number"
    else:
        return "not an armstrong number" 

print(is_armstrog_number(1634))
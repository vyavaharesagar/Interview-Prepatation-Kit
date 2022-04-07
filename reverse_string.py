# slicing method

# name = "sagar"
# print(name[::-1])


def reverse_string(str):
    s = list(str)
    tmp = []
    for x in reversed(range(len(str))):
        tmp.append(s[x])

    return tmp.join(tmp)

    


print(reverse_string("sagar"))

def find_median(arr):
    arr.sort()
    return arr[int(len(arr)/2)]


arr = [0,1,2,4,6,5,3]
print(find_median(arr))
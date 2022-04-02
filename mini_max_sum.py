#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    x = max(arr)
    y = min(arr)
    temp = 0
    for i in arr:
        temp +=i
        
    print(temp-x,temp-y) 

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)



# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14



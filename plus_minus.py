#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    x,z,y=0,0,0
    for i in range(len(arr)):
        if arr[i]>0:
            x += 1
        if arr[i]<0:
            y += 1
        if arr[i]==0:
            z += 1
    print(x/len(arr))
    print(y/len(arr))
    print(z/len(arr))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

# Sample Input

# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
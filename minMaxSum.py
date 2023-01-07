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
    total = minimum = maximum = arr[0]
    for i in range(1,5):
        total += arr[i]
        if minimum > arr[i]:
            minimum = arr[i]
        if maximum < arr[i]:
            maximum = arr[i]
    print(total-maximum,total-minimum)
            
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

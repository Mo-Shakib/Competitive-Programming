# https://www.hackerrank.com/challenges/compare-the-triplets/problem
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alic = 0
    bob = 0
    for i, j in zip(a, b):
        if i > j:
            alic += 1
        elif j > i:
            bob += 1
            
    return alic, bob
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

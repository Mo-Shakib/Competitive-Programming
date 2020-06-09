import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
bin_n = bin(n)[2:]
find_ones = bin_n.split('0')
longest_one = len(max(find_ones, key=len))
print(longest_one)

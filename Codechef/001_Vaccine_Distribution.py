# https://www.codechef.com/problems/VACCINE2

from math import ceil

def findRisk(arr, day):
    atRisk = 0
    notRist = 0
    for i in arr:
        if (i <= 9) or (i >= 80):
            atRisk += 1
        else:
            notRist += 1
    time = ceil(atRisk/day) + ceil(notRist/day)
    return time

t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    ns = map(int, input().split())

    print(findRisk(ns, d))
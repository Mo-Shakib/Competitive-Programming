# https://codeforces.com/contest/1409/problem/B
t = int(input())
count = 0
for i in range(t):
    a,b,ax,by, n = map(int, input().split())
    if a > b:
        while a >= b and a >= ax:
            a 

    if (a > b) and (a > ax):
        a = a - 1 * n
    elif (b > a) and (b > by):
        b = b - 1 * n
    print(a * b)


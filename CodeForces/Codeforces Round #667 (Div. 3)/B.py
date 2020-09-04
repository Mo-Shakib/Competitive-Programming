def b_func(a, b, c, d, e):
    count = 0
    while count < n:
        if a >= ax:
            a -= 1
            count += 1
        elif b >= by:
            b -= 1
            count += 1
        elif (a > b and a >= ax) or (b > a and b >= by):
            b -= 1
            count += 1
        elif (a > b and a >= ax) or (b > a and b >= by):
            a -= 1
            count += 1
    print(a * b)
t = int(input())

for i in range(t):
    a,b,ax,by, n = map(int, input().split())
    b_func(a,b,ax,by,n)
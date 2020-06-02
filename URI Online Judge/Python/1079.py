x = int(input())

for i in range(1, (x+1)):
    n = input().split()
    a, b, c = n
    print('{:.1f}'.format((float(a) * 2 + float(b) * 3 + float(c) * 5) / 10))

n = int(input())

a, b, c = 1, 1, 1
count = 0

while count < n:
    print('{0} {1} {2}'.format(a, b, c))
    a += 1
    b = a**2
    c = a**3
    count += 1
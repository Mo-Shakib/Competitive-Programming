n = int(input())
a, b, c = 1, 2, 3
count = 0
while count < n:
    print('{0} {1} {2} PUM'.format(a,b,c))
    a += 4
    b += 4
    c += 4
    count += 1
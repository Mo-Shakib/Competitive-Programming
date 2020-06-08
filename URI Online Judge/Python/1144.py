i = 1
limit = 0
n = int(input())
while limit < n:
    print('{} {} {}'.format(i, (i**2), (i**3)))
    print('{} {} {}'.format(i, (i**2)+1, (i**3)+1))
    i = i + 1
    limit = limit + 1

n = int(input())
x = 0
for j in range(0, 1000, 1):
    print('N[{}] = {}'.format(j, x))
    x += 1
    if x == n:
        x = 0


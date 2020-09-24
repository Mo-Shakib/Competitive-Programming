t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    cubes = list(map(int, input().split()))
    x = len(cubes)
    sortedArray = sorted(cubes)
    for k, l in zip(cubes, sortedArray):
        count += 1
    # print('Change need:', count)
    y = (n * (n - 1)) - 1
    if y >= count:
        print('YES')
    else:
        print('NO')


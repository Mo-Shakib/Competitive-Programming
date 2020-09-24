t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    cubes = list(map(int, input().split()))
    x = len(cubes)
    sortedArray = sorted(cubes)
    for k, l in zip(cubes, sortedArray):
        count += 1 # total changes we need
    
    y = (n * (n - 1)) - 1 # exchanges we can make
    if y >= count:
        print('YES')
    else:
        print('NO')


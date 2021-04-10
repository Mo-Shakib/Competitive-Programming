t = int(input())
for i in range(t):
    size = int(input())
    arr = list(map(int, input().split()))
    
    s_arr = sorted(arr)

    n = s_arr[0]
    m = s_arr[-1]

    a = 0
    b = 0

    for j in s_arr:
        if n == j:
            a += 1
        elif m == j:
            b += 1
    
    if a == 1:
        print(arr.index(n)+1)
    else:
        print(arr.index(m)+1)

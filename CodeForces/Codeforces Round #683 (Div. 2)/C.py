t = int(input())

for i in range(t):
    total = 0
    count = 0
    count2 = 0
    db = 0

    n, w = map(int, input().split())
    wi = list(map(int, input().split()))

    lim = w/2
    idx = []
    y = len(wi)

    z = [x for x in range(1, y+1)]
    
    for k in wi:
        if (k <= w) and (total <= w):
            total += k
        if total > w:
            break

    for i, ix in zip(wi,z):
        db += i
        if (lim <= total <= w) and (i <= w):
            count += 1
            count2 += 1
            idx.append(ix)

    
    if count == 0:
        print(-1)
    elif count > 0:
        print(count)
    if count2 != 0:
        print(' '.join(map(str, idx)))
    

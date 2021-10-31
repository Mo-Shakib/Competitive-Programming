n, k = map(int, input().split())
wands = list(map(int, input().split()))
wands = sorted(wands)
count = 0
for i in wands:
    for j in wands:
        if abs(i-j) > k:
            count += 1
        else:
            break

if count % 2 == 0:
    print(count//2)
else:
    print(count)
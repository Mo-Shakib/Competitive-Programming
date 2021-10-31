n, k = map(int, input().split())
wands = list(map(int, input().split()))

wands = sorted(wands)

count = 0

x = 0
y = -1
for i in range(len(wands)):
    if (wands[-1] - wands[0]) > k:
        count += 2    
    x += 1
    y -= 1
    
print(count)
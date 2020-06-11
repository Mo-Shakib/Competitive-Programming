a = int(input())
b = int(input())
if a > b:
    maxv = a
    minv = b
else:
    minv = a
    maxv = b

total = 0
for i in range(minv, maxv+1):
    if (i % 13 == 0):
        continue
    total += i
print(total)

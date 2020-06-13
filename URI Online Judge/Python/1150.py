# 1150 - Exceeding Z
t = int(input())
while True:
    n = int(input())
    if n > t:
        break
maxv = n
minv = t
count = 0
j = 0
for i in range(minv, maxv**2, 1):
    j += i
    count += 1
    if j >= maxv:
        break
    
print((count))




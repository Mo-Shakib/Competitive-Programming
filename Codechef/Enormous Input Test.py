# 

count = 0
n, k = map(int, input().split())
for i in range(n):
    ti = int(input())
    if ti % k == 0:
        count += 1
print(count)


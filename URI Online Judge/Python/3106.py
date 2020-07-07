# 3106 - Coding Competition | URI Online Judge

n = int(input())
l = list(map(int, input().split()))
count = 0
x = 0
count1 = 0
result = 0
while count1 < n:
    while True:
        x = l[count]
        x //= 3
        x *= 3
        count += 1
        break
    count1 += 1
    result += x
print(result)


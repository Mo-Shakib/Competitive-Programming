n, k = map(int, input().split())
timeLeft = 240 - k

x = 0
for i in range(1, n+1):
    if timeLeft >= i*5:
        x += 1
        timeLeft -= i*5

print(x)
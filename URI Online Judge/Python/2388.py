t = int(input())
total = 0
for i in range(t):
    a, b = map(int, input().split())
    result = a * b
    total += result
print(total)

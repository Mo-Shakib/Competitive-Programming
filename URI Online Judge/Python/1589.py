t = int(input())
count = 0

while True:
    a, b = map(int, input().split())
    print(a+b)
    count += 1
    if count == t:
        break

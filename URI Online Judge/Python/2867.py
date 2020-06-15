t = int(input())
count = 0
while True:
    n, m = map(int, input().split())

    digit = n ** m
    output = len(str(digit))
    print(output)
    count += 1
    if count == t:
        break

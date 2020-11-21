# https://codeforces.com/problemset/problem/791/A
a, b = map(int, input().split())

count = 0
while True:
    a *= 3
    b *= 2
    count += 1
    if a > b:
        print(count)
        break
# https://codeforces.com/contest/1409/problem/A
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    diffrence = abs(a-b)
    move_1 = diffrence // 10
    moves = diffrence % 10
    if diffrence % 10 == 0:
        temp = 0
    else:
        temp = 1
    total = move_1 + temp
    print(total)
# success :D
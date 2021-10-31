# https://cses.fi/problemset/task/1094

n = int(input())
x = list(map(int, input().split()))
y = sorted(x)

moves = 0

for i, j in zip(x, y):
    if x != y:
        moves += 1
print(moves)
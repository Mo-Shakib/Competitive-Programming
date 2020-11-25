# http://codeforces.com/problemset/problem/977/A
number, steps = map(int, input().split())

for i in range(steps):

    if str(number)[-1] == '0':
        number //= 10
    else:
        number -= 1

print(int(number))

# Accepted
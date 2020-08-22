# n = question, x = how many, t = time
n, x, t = map(int, input().split())
rate = abs(x-t)
re = abs(n - rate)
print(re)
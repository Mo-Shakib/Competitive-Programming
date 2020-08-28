# https://toph.co/p/fair-distribution
x, y = map(int, input().split())
n = y % x
r = x - n
print(r)
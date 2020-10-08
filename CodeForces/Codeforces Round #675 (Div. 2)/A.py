# https://codeforces.com/contest/1422/problem/0
def find_x(a,b,c):
    x = (((a**2)-(b**2)) + c**2) * 0.5
    print(int(x))
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    find_x(a, b, c)

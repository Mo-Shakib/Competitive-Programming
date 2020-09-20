# https://codeforces.com/problemset/problem/282/A
n = 0
for i in range(int(input())):
    k = input()
    if k[0] == '+' or k[1] == '+':
        n+=1
    else:
        n-=1
print(n)

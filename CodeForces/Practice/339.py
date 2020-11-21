# https://codeforces.com/problemset/problem/339/A

sums = input().split('+')
sums = list(map(int, sums))
sums = sorted(sums)
print('+'.join(map(str, sums)))

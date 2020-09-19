# https://atcoder.jp/contests/abc179/tasks/abc179_b
t = int(input())
count = 1
result = 0
test = 0
p = ''
for i in range(t):
    a, b = map(int, input().split())
    
    if (a == b):
        result = 1
    else:
        result = 0
    
    if result == 1:
        test += 1
        if test >= 3:
            p = 'Yes'
    else:
        test = 0

if p == 'Yes':
    print('Yes')
else:
    print('No')
        


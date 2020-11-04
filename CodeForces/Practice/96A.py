# http://codeforces.com/problemset/problem/96/A

players = input()
count1 = ''
count0 = ''

for i in players:
    if i == '0':
        count1 += '.'
    else:
        count1 += i
        
for j in players:
    if j == '1':
        count0 += '.'
    else:
        count0 += j

count0 = count0.split('.')
count1 = count1.split('.')

n = 0
m = 0
for k in count0:
    if len(k) > 6:
        n += 1
    else:
        m += 1
        
for l in count1:
    if len(l) >= 7:
        n += 1
    else:
        m += 1

if n != 0:
    print('YES')
else:
    print('NO')
    
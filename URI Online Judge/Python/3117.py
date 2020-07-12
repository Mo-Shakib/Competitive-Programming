a, b = map(int, input().split())
students = list(map(int, input().split()))
count = 0
for i in students:
    if i <= 0:
        count += 1
if count >= b:
    print('YES')
else:
    print('NO')


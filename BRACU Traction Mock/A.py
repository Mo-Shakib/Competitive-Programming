t = int(input())
table = []
for j in range(1, 11):
    for k in range(1, 11):
        table.append(j * k)
for i in range(t):
    num = int(input())
    if num in table:
        print('Yes')
    else:
        print('No')
    
    
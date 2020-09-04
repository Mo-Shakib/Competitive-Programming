def func(x):
    table = []
    for j in range(1, 11):
        for k in range(1, 11):
            table.append(j * k)
    if x in table:  out = 'Yes'
    else:   out = 'No'
    print(out)

t = int(input())
for i in range(t):
    num = int(input())
    func(num)
result = 0
b = 1
for i in range(1, 40, 2):
    m = i / b
    result += m
    b = b  ** 2
print('{:.2f}'.format(result))

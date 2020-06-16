a = 0
n = float(input())
print('N[0] = {:.4f}'.format(n))
for i in range(1, 100):
    b = n / 2
    n = b
    print('N[{}] = {:.4f}'.format(i, b))
    

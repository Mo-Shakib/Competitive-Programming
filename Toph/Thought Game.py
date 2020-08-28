t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = (a+b)//2
    if c % 2 == 0:
        print('Sadia will be happy.')
    else:
        print('Oops!')
    
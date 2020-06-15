one, two = map(int, input().split())

if (one == 0) and (two == 0 or two == 1):
    print('C')
elif (one == 1) and (two == 0):
    print('B')
else:
    print('A')

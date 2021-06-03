t = int(input()) # taking input limite

for i in range(t):
    x, y = map(int, input().split())

    # Rafael = (3x)^2 + y^2
    # Beto = 2(x^2) + (5y)^2
    # Carlos = -100x + y^3

    a = (3*x)**2 + y**2
    b = 2 * (x**2) + (5 * y)** 2
    c = (-100)* x + y ** 3

    result = max(a, b, c)

    if result == a:
        print('Rafael ganhou')
    elif result == b:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')

# Accepeted
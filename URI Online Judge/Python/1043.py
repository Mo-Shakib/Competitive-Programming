a, b, c = map(float, input().split())

if (a < b + c and b < a + c and c < a + b):
    print("Perimetro = %.1f"%(a+b+c))
else:
    tra = ((a + b)/2)*c
    print("Area = %.1f"%tra)
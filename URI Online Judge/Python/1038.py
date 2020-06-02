X, Y = map(int, input().split())

if X == 1:
    print("Total: R$ %.2f" %(Y*4))
elif X == 2:
    print("Total: R$ %.2f" %(Y*4.50))
elif X == 3:
    print("Total: R$ %.2f" %(Y*5))
elif X == 4:
    print("Total: R$ %.2f" %(Y*2))
elif X == 5:
    print("Total: R$ %.2f" %(Y*1.50))

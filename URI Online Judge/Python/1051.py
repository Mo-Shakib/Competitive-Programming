amount = float(input())



if 0 < amount <= 2000:
    print("Isento")

elif 2000 < amount <= 3000:
    t = amount - 2000
    tax = t * 8 / 100
    print("R$ %.2f"%tax)

elif 3000 < amount <= 4500:
    t = amount - 2000
    t1 = t - 1000
    tax1 = 1000 * 8 / 100
    tax2 = t1 * 18 / 100
    print("R$ %.2f"%(tax1+tax2))

elif 4500 < amount:
    t = amount - 2000
    t1 = t - 1000
    tax1 = 1000 * 8 / 100
    t2 = t1 - 1500
    tax2 = 1500 * 18 / 100
    tax3 = t2 * 28 / 100

    
    print("R$ %.2f"%(tax1+tax2+tax3))
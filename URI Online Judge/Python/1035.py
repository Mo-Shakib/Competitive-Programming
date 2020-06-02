# 1035 - Selection Test 1
numbers = input().split()

A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])
D = int(numbers[3])

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

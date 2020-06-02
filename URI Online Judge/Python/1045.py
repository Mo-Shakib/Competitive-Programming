a, b, c = map(float, input().split())

list1 = [a, b, c]
list2 = sorted(list1, reverse=True)

A = list2[0]
B = list2[1]
C = list2[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif (A*A) == (B*B) + (C*C):
    print("TRIANGULO RETANGULO")
elif (A*A) > ((B*B) + (C*C)):
    print("TRIANGULO OBTUSANGULO")
elif (A*A) < ((B*B) + (C*C)):
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
elif (A == B != C) or (B == C != A) or (C == A != B):
    print("TRIANGULO ISOSCELES") 
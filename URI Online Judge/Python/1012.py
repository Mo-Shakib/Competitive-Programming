# Taking 3 floating point input
urerinput = input().split(" ")

A, B, C = urerinput
pi = 3.14159
# a) area of triangle
tri = 1/2 * (float(A) * float(C))
# b) area of circle
cir = pi * float(C) ** 2
# c) area of the trapezium
tra = float(C) * (float(A) + float(B)) / 2
# d) area of ​​the square
squ = float(B) ** 2
# e) area of the rectangle
rec = float(A) * float(B)

# Outputs
print("TRIANGULO: %.3f"% tri)
print("CIRCULO: %.3f"% cir)
print("TRAPEZIO: %.3f"% tra)
print("QUADRADO: %.3f"% squ)
print("RETANGULO: %.3f"% rec)
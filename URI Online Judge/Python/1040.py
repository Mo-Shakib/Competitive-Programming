a, b, c, d = map(float, input().split())

avg1 = (a*2 + b*3 + c*4 + d*1)/10

print("Media: %.1f" %avg1)

if avg1 >= 7.0:
    print("Aluno aprovado.")

if avg1 < 5.0:
    print("Aluno reprovado.")

if (5.0 <= avg1 <= 6.9):
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: %.1f" %e)
    avg1 = (avg1 + e) / 2

    if (avg1 >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.") 

    print("Media final: "+str(avg1))

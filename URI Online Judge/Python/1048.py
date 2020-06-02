# 1048 - Salary Increase
salary = float(input())

if 0 < salary <= 400:
    bonus = salary * 15 / 100
    print("Novo salario: %.2f"%(salary+bonus))
    print("Reajuste ganho: %.2f"%bonus)
    print("Em percentual: 15 %")

elif 400 < salary <= 800:
    bonus = salary * 12 / 100
    print("Novo salario: %.2f"%(salary+bonus))
    print("Reajuste ganho: %.2f"%bonus)
    print("Em percentual: 12 %")

elif 800 < salary <= 1200:
    bonus = salary * 10 / 100
    print("Novo salario: %.2f"%(salary+bonus))
    print("Reajuste ganho: %.2f"%bonus)
    print("Em percentual: 10 %")

elif 1200 < salary <= 2000:
    bonus = salary * 7 / 100
    print("Novo salario: %.2f"%(salary+bonus))
    print("Reajuste ganho: %.2f"%bonus)
    print("Em percentual: 7 %")

elif 2000 < salary:
    bonus = salary * 4 / 100
    print("Novo salario: %.2f"%(salary+bonus))
    print("Reajuste ganho: %.2f" %bonus)
    print("Em percentual: 4 %")


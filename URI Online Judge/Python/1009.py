name = str(input())
fixed_salary = float(input())
seles = float(input())

bonus = (seles * 15)/100
final_salary = fixed_salary + bonus

print('TOTAL = R$ %.2f' %final_salary)


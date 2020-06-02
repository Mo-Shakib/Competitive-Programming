# Banknotes
amount = int(input())
print(amount)

print('{} nota(s) de R$ 100,00'.format(int(amount/100)))
left_money = amount % 100
print('{} nota(s) de R$ 50,00'.format(int(left_money/50)))
left_money = left_money % 50
print('{} nota(s) de R$ 20,00'.format(int(left_money/20)))
left_money = left_money % 20
print('{} nota(s) de R$ 10,00'.format(int(left_money/10)))
left_money = left_money % 10
print('{} nota(s) de R$ 5,00'.format(int(left_money/5)))
left_money = left_money % 5
print('{} nota(s) de R$ 2,00'.format(int(left_money/2)))
left_money = left_money % 2
print('{} nota(s) de R$ 1,00'.format(int(left_money/1)))

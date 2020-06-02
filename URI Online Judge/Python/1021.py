# 2021 - Banknotes and Coins

amount = float(input())

print('NOTAS:')
print("{} nota(s) de R$ 100.00".format(int(amount / 100)))
left_money = amount % 100
print('{} nota(s) de R$ 50.00'.format(int(left_money/50)))
left_money = left_money % 50
print('{} nota(s) de R$ 20.00'.format(int(left_money/20)))
left_money = left_money % 20
print('{} nota(s) de R$ 10.00'.format(int(left_money/10)))
left_money = left_money % 10
print('{} nota(s) de R$ 5.00'.format(int(left_money/5)))
left_money = left_money % 5
print('{} nota(s) de R$ 2.00'.format(int(left_money/2)))
left_money = left_money % 2

print('MOEDAS:')
left_money2 = left_money * 100 # multiply rest of the noates to get int numbers
print('{} moeda(s) de R$ 1.00'.format(int(left_money2/100)))
left_money2 = left_money2 % 100
print('{} moeda(s) de R$ 0.50'.format(int(left_money2/50)))
left_money2 = left_money2 % 50
print('{} moeda(s) de R$ 0.25'.format(int(left_money2/25)))
left_money2 = left_money2 % 25
print('{} moeda(s) de R$ 0.10'.format(int(left_money2/10)))
left_money2 = left_money2 % 10
print('{} moeda(s) de R$ 0.05'.format(int(left_money2/5)))
left_money2 = left_money2 % 5
print('{} moeda(s) de R$ 0.01'.format(int(left_money2)))



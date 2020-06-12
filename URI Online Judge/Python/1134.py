count = 'yes'
alcohol = 0
gasoloin = 0
diesel = 0
while count == 'yes':
    feul = int(input())
    if feul == 1:
        alcohol += 1
    elif feul == 2:
        gasoloin += 1
    elif feul == 3:
        diesel += 1
    elif feul == 4:
        break
    else:
        count = 'yes'

print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(alcohol, gasoloin, diesel))
t = int(input())
count = 0
for test in range(t):
    a, b = map(str, input().split())
    count += 1
    for game in range(1):
        if a == 'tesoura' and b == 'papel':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'papel' and b == 'pedra':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'pedra' and b == 'lagarto':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'lagarto' and b =='Spock':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'Spock' and b == 'tesoura':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'tesoura' and b == 'lagarto':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'lagarto' and b == 'papel':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'papel' and b == 'Spock':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'Spock' and b == 'pedra':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == 'pedra' and b == 'tesoura':
            print('Caso #{}: Bazinga!'.format(count))
        elif a == b:
            print('Caso #{}: De novo!'.format(count))
        else:
            print('Caso #{}: Raj trapaceou!'.format(count))

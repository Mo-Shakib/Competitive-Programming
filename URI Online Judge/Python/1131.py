# URI Online Judge - 1131 | Grenais

count = 0
total_match = 0
inter_total = 0
gremio_total = 0
inter_won = 0
gremio_won = 0
drow = 0
while count != 2:
    inter, gremio = map(int, input().split())
    print('Novo grenal (1-sim 2-nao)')
    
    if inter > gremio:
        inter_won += 1
    elif inter < gremio:
        gremio_won += 1
    else:
        drow += 1

    count = int(input())
    total_match += 1
    
print('{} grenais'.format(total_match))
print('Inter:{}'.format(inter_won))
print('Gremio:{}'.format(gremio_won))
print('Empates:{}'.format(drow))

if inter_won > gremio_won:
    print('Inter venceu mais')
elif inter_won < gremio_won:
    print('Gremio venceu mais')
elif inter_won == gremio_won:
    print('Nao houve vencedor')




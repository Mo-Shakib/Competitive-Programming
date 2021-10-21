a = list(map(int, input().split()))
L = a[0]
S = a[1]
ludder = []
snake = []
for i in range(L):
    x, y = map(int, input().split())
    ludder.append((x, y))
for j in range(S):
    p, q = map(int, input().split())
    snake.append((p,q))
    

ludder_start = []
ludder_end = []
snake_start = []
snake_end = []

for i in ludder:
    ludder_start.append(i[0])
    ludder_end.append(i[1])

for j in snake:
    snake_start.append(j[0])
    snake_end.append(j[1])

jaber = 0
mukhter  = 0
n = -1

while True:
    v = int(input())
    n += 1
    if n % 2 == 0:
        if jaber != 0:
            jaber += v
            if jaber in ludder_start:
                val_index = ludder_start.index(jaber)
                jaber = ludder[val_index][1]
            elif jaber in snake_start:
                val_index2 = snake_start.index(jaber)
                jaber = snake[val_index2][1]
        
        elif v == 1 and jaber == 0:
            jaber += 1
    
    elif n % 2 == 1:
        if mukhter != 0:
            mukhter += v
            if mukhter in ludder_start:
                val_index3 = ludder_start.index(mukhter)
                mukhter = ludder[val_index3][1]
            elif mukhter in snake_start:
                val_index4 = snake_start.index(mukhter)
                mukhter = snake[val_index4][1]
        
        elif v == 1 and mukhter == 0:
            mukhter += 1
        
    if mukhter >= 100:
        print('Mukhter Hossain is the winner.')
        break
    if jaber >= 100:
        print('Jaber Tuhin is the winner.')
        break
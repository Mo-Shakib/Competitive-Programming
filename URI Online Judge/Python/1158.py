t = int(input())
count = 0
while True:
    a, b = map(int, input().split())
    
    if a % 2 == 1:
        start = a
    else:
        start = a + 1
    l = []
    count2 = 0
    for i in range(start, start + 2*b, 2):
        l.append(i)
        count2 += 1
        if count2 == b:
            break

    print(sum(l))
    count += 1
    if count == t:
        break
# or 
t = int(input())
count = 0
while True:
    a, b = map(int, input().split())
    
    if a % 2 == 1:
        start = a
    else:
        start = a + 1
    l = []
    for i in range(start, start + 2*b, 2):
        l.append(i)
    
    print(sum(l))
    count += 1
    if count == t:
        break

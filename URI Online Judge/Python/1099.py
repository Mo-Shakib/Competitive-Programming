tc = int(input())
for pos in range(0,tc):
    a,b = input().split()
    a,b = [int(a),int(b)]
    if a > b:
        a,b = b,a
    if a % 2 == 0:
        a += 1
    else:
        a += 2
    sum = 0
    for i in range(a,b,2):
        sum += i
    print(sum)
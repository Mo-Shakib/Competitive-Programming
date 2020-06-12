x, y = map(int, input().split())
count = 0
while count < (y//x):
    start = count*x + 1
    end = (count + 1) * x + 1
    for i in range(start,end,1):
        print(i,end=" ")
    print("")
    count+=1

x, y = map(int, input().split())
count = 0
while count < y // x:
    start = count * x + 1
    end = start + x

    print(*range(start, end), sep=" ")

    count += 1
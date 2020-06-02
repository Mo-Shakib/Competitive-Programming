limit = int(input())
odd = 0
if 1 <= limit <= 1000:

    for i in range(1, (limit+1)):
        if (i % 2 == 1):
            print(i)


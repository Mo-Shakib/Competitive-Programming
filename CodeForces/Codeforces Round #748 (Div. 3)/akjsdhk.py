n = '12345'
for i in range(len(n)-1, -1, -1):
    # print(n[i])
    print('i =',i)
    for j in range(i, -1, -1):
        print('j =',j)
        print('Value:',n[j])
        
        
n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
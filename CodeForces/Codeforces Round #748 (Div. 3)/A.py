for i in range(int(input())):
    l = list(map(int, input().split()))
    a = l[0]
    b = l[1]
    c = l[2]
    if max(l) == 0:
        print('1 1 1')
    else:
        top = max(l)
        temp = 0
        for j in l:
            if j == top:
                temp += 1
        if temp > 1:
            print(f'{top-a+1} {top-b+1} {top-c+1}')    
        else:
            if top == a:
                print(f'{0} {top-b+1} {top-c+1}')    
            elif top == b:
                print(f'{top-a+1} {0} {top-c+1}')
            elif top == c:
                print(f'{top-a+1} {top-b+1} {0}')
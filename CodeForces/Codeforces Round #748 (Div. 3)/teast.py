    # Working
def solution(n):
    removed = []
    print(n)
    found = []
    div = ['00', '25', '50', '75']
    for i in range(len(n)-1, -1, -1):
        x = ''
        if int(n[i]) in [0, 5] and len(x) < 3:
            x += n[i]
            if int(n[i]) == 5:
                x += n[i]
                for j in range(i, -1, -1):
                    if int(n[j]) in [2, 7] and len(x) < 2:
                        x += n[j]
                        found.append(x[::-1])
                        break
                    
            elif int(n[i]) == 0 and len(x) < 2:
                x += n[i]
                for j in range(i, -1, -1):
                    if int(n[j]) in [0, 5] and len(x) < 2:
                        x += n[j]
                        found.append(x[::-1])
                        break
            else:
                removed.append(int(n[i]))
        else:
            removed.append(int(n[i]))
    # return len(removed)
    print(found)
    print(len(removed))

# solution('70005')
solution('100')
solution('71345')
solution('3259')
solution('50555')
solution('2050047')
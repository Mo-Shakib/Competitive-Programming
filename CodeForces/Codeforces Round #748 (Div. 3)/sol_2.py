def solution(n):
    n = n[::-1]
    removed = []
    print(n)
    found = []
    for i in range(len(n)):
        if int(n[i]) in [0, 5]:
            if int(n[i]) == 5:
                for j in range(i, len(n)):
                    if int(n[i]) in [2, 7]:
                        found.append(1)
                        break
            elif int(n[i]) == 0:
                for j in range(i, len(n)):
                    if int(n[i]) in [0, 5]:
                        found.append(1)
                        break
            else:
                removed.append(int(n[i]))
        elif len(found) > 1:
            break
        else:
            removed.append(int(n[i]))
    return len(removed)



print(solution('50555'))
    
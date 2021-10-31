

def main(n):
    lenth = len(n)
    ans = []
    for i in range(lenth):
        for j in range(i+1, lenth):
            # print(f'value: i = {n[i]}, j = {n[j]}')
            # print(f'Index: {i} -> {n[i]}, {j} -> {n[j]}')
            
            if (int(n[i])*10 + int(n[j])) % 25 == 0:
                print(f'Index: {i} -> {n[i]}, {j} -> {n[j]} = YES [{int(n[i])*10 + int(n[j])}]')
                # print(f'index i = {i}, j = {j} - YES')
                # print(n[i:j+1])
                # print(int(n[i:j+1]))
                # print(f'haha: {int(n[i])*10 + int(n[j])}')
                # a = int(n[:j+1])
                a = int(n[i])*10 + int(n[j])
                # print('a = ', a)
                res = lenth - len(str(a))
                print('Res:',res)
                # print('res = ', res)
                ans.append(res)

    print(f'Result: {min(ans)}')


# main('71345')
main('100')
# main('50555')

# main('2050047')
# https://vjudge.net/contest/472762?fbclid=IwAR33bcT3Du8Y9V6YOtSbY-ULpZuUis3fWp4VjYUI3H_zx52G9iEoaax-tas#problem/A

def dec_to_bin(x):
    a = '00000000'
    b = str(bin(x)[2:])
    return (a + b)[-8:]


def solution(int_value):
    ip_adrr = list(map(int, int_value.split('.')))
    ip = ''
    for i in ip_adrr:
        ip += str(dec_to_bin(i))
        ip += '.'
    return ip[:-1]
        

n = int(input())
for i in range(n):
    x = input()
    x = solution(x)
    y = input()
    
    if x == y:
        print(f'Case {i+1}: Yes')
    else:
        print(f'Case {i+1}: No')
    
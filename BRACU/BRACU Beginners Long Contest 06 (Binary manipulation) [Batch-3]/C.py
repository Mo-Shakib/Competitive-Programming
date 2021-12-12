# https://vjudge.net/contest/472762#problem/C

# getting the position of the least significant digit
def pos_lsd(num):
    x = bin(num)[2:]
    return len(str(x))

def solution(arr):
    my_dict = {}
    result = 0
    
    for i in arr:
        idx = pos_lsd(i)
        if idx not in my_dict:
            my_dict[idx] = [i]
        else: my_dict[idx] += [i]

    for x in my_dict.values():
        if len(x) > 1:
            result += (len(x)*(len(x)-1)//2)
    
    return result
        
n = int(input())
for i in range(n):
    a = int(input())
    x = list(map(int, input().split()))
    print(solution(x))
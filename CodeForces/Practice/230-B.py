# https://codeforces.com/problemset/problem/230/B
def result(n):
    i = 2
    factors = []
    while n >= 2 and len(factors) <= 3: 
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    if (len(factors) == 2) and (factors[0] == factors[-1]):
        print('YES')
    else:
        print('NO')

c = int(input())
p_ints = list(map(int, input().split()))

for n in p_ints:
    try:
        result(n)
    except IndexError:
        print('NO')
    

# limit = 1000000
# def calculate_prime():
#     prime_flag = [True] * limit
#     prime_flag[0] = prime_flag[1] = False
#     for i in range(2,limit):
#         if prime_flag[i] == True:
#             for j in range(i*i, limit, i):
#                 prime_flag[j] = False
#     return prime_flag                    

# def check_if_a_number_is_t_prime(n):
#     if n == 4:
#         return True
#     if n < 4 or n%2==0:
#         return False
#     sqrt_n = n**0.5
#     if sqrt_n==int(sqrt_n):
#         if prime_flag[int(sqrt_n)] == True:
#             return True
#     return False

# prime_flag = calculate_prime()

# total_numbers = int(input())
# input_array = list(map(int,input().split()))
# for i in input_array:
#     if check_if_a_number_is_t_prime(i)==True:
#         print("YES")
#     else:
#         print("NO")
        
    

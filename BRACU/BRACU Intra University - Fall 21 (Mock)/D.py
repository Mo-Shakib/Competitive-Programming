def solution(n):
    if n == 0:
        return 'The number 0 is neutral.'
    if n % 2 == 0:
        return f'The number {n} is even.'
    return f'The number {n} is odd.'

print(solution(int(input())))

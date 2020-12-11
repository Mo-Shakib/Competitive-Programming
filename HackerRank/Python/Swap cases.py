# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    x = ''
    for char in s:
        if char.isupper():
            x += char.lower()
        elif char.islower():
            x += char.upper()
        else:
            x += char

    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
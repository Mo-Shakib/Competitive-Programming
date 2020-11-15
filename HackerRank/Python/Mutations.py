# https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    out = ''
    for i in range(len(string)):
        if i == position:
            out += character
        else:
            out += string[i]
        
    return out

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
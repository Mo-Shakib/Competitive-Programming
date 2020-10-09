# https://www.hackerrank.com/challenges/python-lists/problem
main = []
t = int(input())

for i in range(t):
    tokens = input().split()

    if tokens[0] == 'insert':
        main.insert(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'print':
        print(main)
    elif tokens[0] == 'remove':
        main.remove(int(tokens[1]))
    elif tokens[0] == 'append':
        main.append(int(tokens[1]))
    elif tokens[0] == 'sort':
        main.sort()
    elif tokens[0] == 'pop':
        main.pop()
    elif tokens[0] == 'reverse':
        main.reverse()
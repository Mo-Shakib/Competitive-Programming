# https://codeforces.com/problemset/problem/58/A

def findChat(string):
    arr = ['h','e','l','l','o']
    output = ''
    count = 0
    
    for char in string:
        if char in arr[0+count:1+count]:
            count += 1
            output += char
    
    if output == 'hello':
        return 'YES'
    
    return 'NO'

print(findChat(input()))
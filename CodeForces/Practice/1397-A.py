# https://codeforces.com/contest/1397/problem/A
for i in range(int(input())):
    mystring = ''
    dict = {}
    for j in range(int(input())):
        string = input()
        mystring += string
    mystring = list(map(str,mystring))

    for i in mystring:
        if i in dict:
            dict[i] += 1
            temp = dict[i]
        else:
            dict[i] = 1
    
    temp2 = 0
    for i in dict.values():
        if (i == temp) or (i == temp*2) or (i == temp // 2):
            temp2 += 1

    
    if temp2 == len(dict):
        print('YES')
    else:
        print('NO')



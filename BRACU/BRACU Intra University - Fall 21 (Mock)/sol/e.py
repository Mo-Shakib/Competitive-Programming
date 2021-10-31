def listToString(s): 
    str1 = " " 
    return (str1.join(s))
        
t = int(input())
cards = []
for i in range(t):
    x = list(input().split())
    if x[0] == 'insert':
        cards.append(listToString(x[1:]))
    elif x[0] == 'peek':
        print(cards[-1])
    elif x[0] == 'size':
        print(len(cards))
    elif x[0] == 'drop':
        cards.pop()

    
def solution(key, word):
    total = 0
    dic = {}
    for i in range(1, len(key)+1):
        dic[key[i-1]] = i
    for x in range(len(word)-1):
        total += abs(dic[word[x]] - dic[word[x+1]])
    print(total)

n = int(input())
keybord = []
for i in range(n):
    key = input()
    word = input()        
    solution(key, word)
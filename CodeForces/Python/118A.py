text = input().lower()
vowel = 'aeiou'
for i in vowel:
    text = text.replace(i,'')
result = ''
for j in text:
    result += '.'+ j
print(result)

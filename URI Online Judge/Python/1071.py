x = int(input())
y = int(input())

if x > y:
    max = x
    min = y
else:
    max = y
    min = x

odd = 0
for i in range((min+1), max): 
    if (i % 2 == 1):
        odd = odd + i
print(odd)



l = []
result = 0
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))

for i in l:
    if (float(i)>0):
        result = result + 1
print(result, "valores positivos")
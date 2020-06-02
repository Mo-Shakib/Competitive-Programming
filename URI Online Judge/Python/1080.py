position = 0
max_value = 0

for i in range(1, 6):
    n = int(input())
    if n > max_value:
        max_value = n
        position = i
        
print("{}\n{}".format(max_value, position))



def Cycle(i, j):
    max_length = 0
    for n in range(i, j+1):
        cycle = []
        while(True):
            cycle.append(n)
            if(n==1):
                break
            if(n%2==0):
                n = n//2
            else:
                n = (3*n)+1
        if(max_length < len(cycle)):
            max_length = len(cycle)
         
    return max_length

Z = input().split(" ")
i = int(Z[0])
j = int(Z[1])

cycle_length = Cycle(i, j)
print(i, j, cycle_length)
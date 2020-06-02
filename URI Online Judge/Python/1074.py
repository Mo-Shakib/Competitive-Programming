x = int(input())
l = []
if x < 10000:
    for pos in range(0, (x)): # This range indicates that how many input will be read
        l.append(int(input()))
    for i in l:
        if (i%2!=0) and (i<0):
            print("ODD NEGATIVE")
        elif(i%2!=0) and (i>0):
            print("ODD POSITIVE")
        elif(i%2==0) and (i<0):
            print("EVEN NEGATIVE")
        elif(i%2==0) and (i>0):
            print("EVEN POSITIVE")
        elif(i==0):
            print("NULL")

    

n=int(input())
a= [2,3,5,7]
i=3
j=9
while i<n:
        flag=0
        j=j+2
        for k in range(len(a)):
            if (a[k]<=int(j**0.5) and j%a[k]==0):
                flag=1
                break
        if flag==0:
            a=a+[j]
            i=i+1
print(a[n-1])

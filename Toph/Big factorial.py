# https://toph.co/p/big-factorials
n = int(input())
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
print (str(fact)[-4:])

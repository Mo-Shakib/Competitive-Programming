# Below is Pythone code for input/output
 
import sys
# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = sys.stdin.readline()
for i in range(1, n):
    sys.stdout.write(i)    
    


# print(a)

# Printing the Output to output.txt file

sys.stdout.close()
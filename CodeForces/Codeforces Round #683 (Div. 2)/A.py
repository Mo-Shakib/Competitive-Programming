# https://codeforces.com/contest/1447/problem/0
# t = int(input())
# for i in ramge(t):
#     n = int(input())

# Python3 program to implement 
# the above approach 
from collections import defaultdict 

# Function to find largest 
# subarray with no dublicates 
def largest_subarray(a, n): 

	# Stores index of array elements 
	index = defaultdict(lambda : 0) 
	
	ans = 0
	j = 0

	for i in range(n): 

		# Update j based on previous 
		# occurrence of a[i] 
		j = max(index[a[i]], j) 

		# Update ans to store maximum 
		# length of subarray 
		ans = max(ans, i - j + 1) 

		# Store the index of current 
		# occurrence of a[i] 
		index[a[i]] = i + 1

		i += 1

	# Return final ans 
	return ans 

# Driver Code 
arr = [ 1, 1, 2, 2, 3, 3, 3] 
n = len(arr) 

# Function call 
print(largest_subarray(arr, n)) 

# This code is contributed by Shivam Singh 

# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    N = len(string) 
    M = len(sub_string) 
    res = 0
      
    # A loop to slide pat[] one by one  
    for i in range(N - M + 1): 
          
        # For current index i, check  
        # for pattern match  
        j = 0
        while j < M: 
            if (string[i + j] != sub_string[j]): 
                break
            j += 1
  
        if (j == M): 
            res += 1
            j = 0
    return res


if __name__ == '__main__':

    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# ABCDCDC
# CDC
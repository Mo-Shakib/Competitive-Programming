# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    x = string.find(sub_string)


    return x

if __name__ == '__main__':

    # string = input().strip()
    string = 'ABCDCDC'
    # sub_string = input().strip()
    sub_string = 'CDC'
    
    count = count_substring(string, sub_string)
    print(count)


# ABCDCDC
# CDC
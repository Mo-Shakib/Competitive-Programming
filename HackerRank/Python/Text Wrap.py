# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap #how to use: https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    tring = wrapper.fill(text=string)
    return tring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
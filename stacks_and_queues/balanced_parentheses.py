"""
Check to see if a sequence of parentheses are balanced.

from https://www.hackerrank.com/challenges/ctci-balanced-brackets
"""
def balance_check(s):
    # O(N) Solution

    if len(s) % 2 != 0:
        return False
    
    stack = []
    corresponding_parentheses = {'}':'{', ']':'[', ')':'('}
    
    for item in s:
        if stack:
            if item in corresponding_parentheses and stack[-1] == corresponding_parentheses[item]:
                stack.pop()
            else:
                stack.append(item)
        else:
            stack.append(item)

            
    return len(stack) == 0

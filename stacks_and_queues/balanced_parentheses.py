"""
Check to see if a sequence of parentheses are balanced.
"""
def balance_check(s):
	# O(N) Solution

    if len(s) % 2 != 0:
        return False
    
    stack = Stack()
    corresponding_parentheses = {'}':'{', ']':'[', ')':'('}
    for item in s:
        if item in corresponding_parentheses and stack.peek == corresponding_parentheses[item]:
            stack.pop()
        else:
            stack.push(item)
    return stack.size == 0
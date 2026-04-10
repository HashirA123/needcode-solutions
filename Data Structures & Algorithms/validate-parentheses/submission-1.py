class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        store = {')' : '(', '}' : '{', ']' : '['}

        for i in range(len(s)):
            if s[i] in store:
                if len(stack) <= 0:
                    return False
                if stack[-1] == store[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        if len(stack) != 0:
            return False
        
        return True
                
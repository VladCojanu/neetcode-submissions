class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l == 0: 
            return True
        if l % 2 == 1:
            return False

        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if len(stack) == 0:
                    return False

                prev = stack.pop()
                if ((c == ')' and prev != '(') 
                    or (c == ']' and prev != '[')
                    or (c == '}' and prev != '{')):
                    return False
        
        return len(stack) == 0

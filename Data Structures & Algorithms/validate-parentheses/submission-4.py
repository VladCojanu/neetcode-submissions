class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l == 0: 
            return True
        if l % 2 == 1:
            return False

        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for c in s:
            if c in close_to_open:
                # pop
                if len(stack) > 0 and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)


        return len(stack) == 0

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-/*":
                second = stack.pop()
                first = stack.pop()
            if t == "+":
                stack.append(first + second)
            elif t == "-":
                stack.append(first - second)
            elif t == "/":
                div = first / second
                div = math.ceil(div) if div < 0 else math.floor(div)
                stack.append(div)
            elif t == "*": 
                stack.append(first * second)
            else: 
                stack.append(int(t))
        
        return stack[0]
        

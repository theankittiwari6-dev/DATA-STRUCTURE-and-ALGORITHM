class Solution:
    def infixToPostfix(self, s):
        # code here
        def priority(ch):
            if ch == "+" or ch == "-":
                return 1
            if ch == "*" or ch == "/":
                return 2
            if ch == "^":
                return 3
            return 0
        
        stack = []
        result = []
        for ch in s:
            if ("a" <= ch <= "z") or ("A" <= ch <= "Z") or ("0" <= ch <= "9"):
                result.append(ch)
            elif ch == "(":
                stack.append(ch)
            elif ch == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] != "(" and 
                (priority(stack[-1]) > priority(ch) or
                (priority(stack[-1]) == priority(ch) and ch != "^"))):
                    result.append(stack.pop())
                stack.append(ch)
            
        while stack:
            result.append(stack.pop())
        return "".join(result)

Solution = Solution()
x = Solution.infixToPostfix("h^m^q^(7-4)")
print(x)

class Solution:
    def postToPre(self, s):
        stack = []
        for ch in s:
            if ch.isalnum():
                stack.append(ch)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()

                new_exp = f"{ch}{operand2}{operand1}"

                stack.append(new_exp)

        return stack[-1]
class Solution:
    def isValid(self, s: str) -> bool:
 
        stack = []
        for bra in s:
            if bra == "(" or bra == "{" or bra == "[":
                stack.append(bra)
            else:
                if len(stack) == 0:
                    return False
                e  = stack.pop()
                if (
                    (bra == ")" and e == "(")
                    or (bra == "}" and e == "{")
                    or (bra == "]" and e == "[")
                ):
                    continue
                else:
                    return False
        return len(stack)==0
            
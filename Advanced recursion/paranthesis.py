class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        lenth = 2*n
        para = [""]*lenth
        def backtrack(i,total,open):
            if i >= lenth: 
                if total == 0:
                    result.append("".join(para))
                    return
            if open < n:
                para[i] = "("
                backtrack(i+1, total+1, open+1)
            if total>0:    
                para[i] = ")"
                backtrack(i+1, total-1, open)

        backtrack(0,0,0)
        return result

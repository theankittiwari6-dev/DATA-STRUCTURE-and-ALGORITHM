class Solution:
    def binstr(self, n):
        # code here
        result = []
        number = ["0"]*n
        def backtrack(i):
            if i == n:
                result.append("".join(number))
                return
            number[i] = "0"
            backtrack(i+1)
            
            number[i] = "1"
            backtrack(i+1)
                
        backtrack(0)
        return result    
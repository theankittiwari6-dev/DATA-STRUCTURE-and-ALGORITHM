class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        char_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        subset = []
        def backtrack (i):
            if i >= len(digits):
                result.append("".join(subset))
                return
            for ch in char_map[digits[i]]:
                subset.append(ch)
                backtrack(i+1)
                subset.pop()
        backtrack(0)
        return result
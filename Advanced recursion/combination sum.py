class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        subset = []
        def fun(i, total):
            if total == target:
                result.append(subset.copy())
                return
            if total>target or i >= len(candidates):
                return 
            subset.append(candidates[i])
            fun(i,total + candidates[i])
            subset.pop()
            fun(i+1,total)
        fun(0,0)
        return result
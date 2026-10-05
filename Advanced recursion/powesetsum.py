# brute force 

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        subset = []
        def fun(i, total):
            if total == target:
                result.append(subset.copy())
                return
            if i>=len(candidates) or total>target:
                return
            subset.append(candidates[i])
            fun(i, total + candidates [i])
            subset.pop()
            fun(i+1, total)
        fun(0,0)
        return result




# optimal solution 

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        subset = []
        def fun(i, total):
            if total == target:
                result.append(subset.copy())
                return
            if i>=len(candidates) or total>target:
                return
            subset.append(candidates[i])
            sum = total + candidates[i]
            fun(i, sum)
            e= subset.pop()
            sum -= e
            fun(i+1, sum)
        fun(0,0)
        return result

        
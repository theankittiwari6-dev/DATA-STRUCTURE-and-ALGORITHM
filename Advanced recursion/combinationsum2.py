# brute force 
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = set()
        subset = []
        def backtrack(i,total):
            if total == target :
                temp = sorted(subset)
                result.add(tuple(temp))
                return
            if i >= len(candidates):
                return
            if total>target:
                return
            subset.append(candidates[i])
            backtrack(i+1,total+candidates[i])
            subset.pop()
            backtrack(i+1,total)
        backtrack(0,0)
        return [list(a) for a in result ]     



    

#     optimal solution 


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        subset = []
        def backtrack(i,total):
            if total == target :
                result.append(subset.copy())
                return
            if i >= len(candidates):
                return
            if total>target:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                backtrack(j+1,total+candidates[j])
                subset.pop()
        backtrack(0,0)
        return result   
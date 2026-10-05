class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        subset = []
        def backtrack(i,total):
            if total == n and len(subset) == k:
                result.append(subset.copy())
                return
            if total > n or len(subset) >= k:
                return
            for j in range(i,10):
                subset.append(j)
                backtrack(j+1, total+j)
                subset.pop()
        backtrack(1, 0)
        return result
        
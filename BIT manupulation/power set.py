class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        total_subset = 1<<n
        for num in range(0,total_subset):
            lst = []
            for i in range(0,n):
                if num & (1<<i) != 0 :
                    lst.append(nums[i])
            result.append(lst)
        return result

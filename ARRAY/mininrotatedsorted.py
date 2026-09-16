# brute force 

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n= len(nums)
        min = nums[0]
        for i in range(0,n):
            if nums[i]<min:
                min = nums[i]
        return min



# optimal solution 

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n= len(nums)
        mini  = float("inf")
        low = 0
        high = n-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid]<=nums[high]:
                mini = min(mini,nums[mid])
                high = mid - 1
            else:
                mini = min(mini,nums[low])
                low = mid+1
        return mini
        
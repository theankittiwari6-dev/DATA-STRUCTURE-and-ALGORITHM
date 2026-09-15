# iterative method 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1



# recursive method 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,target,0,len(nums)-1)
    def binary_search(self,nums,target,low,high):
        if low > high:
            return -1
        mid = (low + high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums,target,mid+1,high)
        else:
            return self.binary_search(nums,target,low,mid-1)
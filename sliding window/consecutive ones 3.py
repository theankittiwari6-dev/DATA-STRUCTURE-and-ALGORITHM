# brute force 


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0
        for i in range(0,n):
            zeros = 0
            for j in range (i,n):
                if nums[j] == 0:
                    zeros +=1
                if zeros>k:
                    break
                maxi = max(maxi, j-i+1)
        return maxi
            

# better solution 


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0
        right = 0
        left = 0
        zeros = 0
        while right<n:
            if nums[right] == 0:
                zeros += 1
            while zeros>k:
                if nums[left]==0:
                    zeros -= 1
                left += 1
            maxi = max(maxi, right-left+1)
            right += 1
        return maxi



# optimal solution 

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0
        right = 0
        left = 0
        zeros = 0
        while right<n:
            if nums[right] == 0:
                zeros += 1
            if zeros>k:
                if nums[left]==0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                maxi = max(maxi, right-left+1)
            right += 1
        return maxi




# brute force

def fun(nums):
     n= len(nums)
     
     max = float("-inf")
     for i in range(0,n):
          total = 0
          for j in range(i,n):
               total = total+nums[j]
               if total > max:
                    max = total
     return max

nums  = [-2,1,-3,4,-1,2,1,-5,4]
print(fun(nums))

# optimal solution 


def maxSubArray(self, nums: List[int]) -> int:
        n= len(nums)
        maxi = float("-inf")
        total = 0
        for i in range(0,n):
            total = total + nums[i]
            if total > maxi:
                maxi = total
            if total < 0:
                total = 0
        return maxi
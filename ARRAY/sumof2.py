# brute force 
def fun(nums,target):
     n = len(nums)
     for i in range(0,n):
          for j in range(i+1,n):
               if nums[i]+nums[j]==target:
                    return [i,j]
nums = [2, 4, 3, 5, 7, 8, 9]
print(fun(nums,7))



# optimal solution 

def twoSum(self, nums: List[int], target: int):
     freq = {}
     n = len(nums)
        
     for i in range(0,n):
          remaining = target - nums[i]
          if remaining in freq:
               return [freq[remaining],i]
          freq[nums[i]] = i

# brute force 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        my_set = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))
        return [list(ans) for ans in my_set]

# better solution 


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = set()
        for i in range(0,n):
            my_set = set()
            for j in range(i+1,n):
                third = -(nums[i]+nums[j])
                if third in my_set:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
        return [list(ans) for ans in result]



# optimal solution 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(0,n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                total_sum = nums[i]+nums[j]+nums[k]
                if total_sum<0:
                    j += 1
                elif total_sum>0:
                    k -= 1        
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    result.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return result
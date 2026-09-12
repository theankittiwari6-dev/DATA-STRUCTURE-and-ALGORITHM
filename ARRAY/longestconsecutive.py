# brute force 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0
        for i in range(0,n):
            num = nums[i]
            count = 1
            while nums[i]+1:
                count += 1
                num = nums[i]+1
            if count>max_count:
                max_count = count
        return max_count



#     better solution 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        last_smallest = float("-inf")
        count = 0
        longest = 0
        for i in range(0,n):
            num = nums[i]
            if num-1 == last_smallest:
                count += 1
                last_smallest = num
            elif num != last_smallest:
                count = 1
                last_smallest = num
            if count>longest:
                longest  =  count
        return longest



# optimal solution 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        n = len(nums)
        for i in range(0,n):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count +=1
                    x +=1
                if count>longest:
                    longest = count
        return longest
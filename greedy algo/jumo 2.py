# brute force 


class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)

        def fun(index):
            if index >= n - 1:
                return 0

            min_jump = float('inf')

            for i in range(1, nums[index] + 1):
                if index + i < n:
                    min_jump = min(
                        min_jump,
                        1 + fun(index + i)
                    )

            return min_jump

        return fun(0)




# optimal Solution 

class Solution:
    def jump(self, nums: list[int]) -> int:
        right = 0
        left = 0
        n = len(nums)
        jump = 0
        while right < n-1:
            far = 0
            for i in range(left, right+1):
                far = max(far, i+nums[i])
            left = right+1
            right = far
            jump += 1
        return jump
        
        
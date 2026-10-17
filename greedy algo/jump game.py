class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_id = 0
        for i in range(0, len(nums)):
            if i > max_id:
                return False
            max_id = max(max_id, i+nums[i])
        return True
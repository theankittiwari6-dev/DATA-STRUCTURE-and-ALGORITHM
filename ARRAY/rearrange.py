# brute froce /
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []
        for i in range(0,n):
            if nums[i]>=0:
                pos.append(nums[i])
            if nums[i]<0:
                neg.append(nums[i])
        for i in range(0,len(pos)):
            nums[2*i]=pos[i]




# optimal solution 

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        list = [0]*n
        posidx = 0 
        negidx = 1
        for i in range (0,n):
            if nums[i]>=0:
                list[posidx]=nums[i]
                posidx+=2
            else:
                list[negidx]=nums[i]
                negidx+=2
        return list
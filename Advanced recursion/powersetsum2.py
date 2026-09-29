class Solution:
    def checkSubsequenceSum(self, arr, k):
        def backtrack(i,total):
            if total == k:
                return True
            if total > k or i >= len(arr):
                return False
            sum = total + arr[i]
            pick = backtrack(i+1,sum)
            if pick == True:
                return True
            sum = total
            not_pick = backtrack(i+1,sum)
            return not_pick
        return backtrack(0,0)
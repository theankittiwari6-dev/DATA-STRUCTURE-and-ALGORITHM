class Solution:
	def perfectSum(self, arr, target):
		def backtrack(i, total):
			if total == target:
			   return 1
		     elif total>target:
		        return 0
		     if i >= len(arr):
		        return 0
            
               pick = backtrack(i+1, total +arr[i])
            
               n_pick = backtrack(i+1, total)
            
               return pick+n_pick

          return backtrack(0,0)
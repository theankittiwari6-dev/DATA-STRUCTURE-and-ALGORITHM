class Solution:
	def subsetSums(self, arr):
		result = []
		subset = []
		def backtrack(i):
		     if i >= len(arr):
		         result.append(sum(subset))
		         return
		     subset.append(arr[i])
		     backtrack(i+1)
		     subset.pop()
		     backtrack(i+1)
	     backtrack(0)
	     return result
		
# brute force


class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        ans = 1
        n = len(arr)
        for i in range(n):
            count = 0
            for j in range(n):
                if arr[j]<=arr[i]<=dep[j]:
                    count += 1
            ans = max(ans, count)
        return ans



# optimal solution 


class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        arr.sort()
        dep.sort()
        ans = 1
        count = 1
        i = 1
        j = 0
        n = len(arr)
        while i<n:
            if arr[i]<=dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans
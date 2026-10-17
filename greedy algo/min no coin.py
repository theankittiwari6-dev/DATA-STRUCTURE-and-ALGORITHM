class Solution:
    def findMin(self, n: int) -> int:
        coins = [1,2,5,10]
        l = len(coins)
        num = 0
        for i in range(l-1,-1,-1):
            while n >= coins[i]:
                num +=1
                n -= coins[i]
        return num
        
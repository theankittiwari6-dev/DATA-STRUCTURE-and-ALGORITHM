# bryte broce 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max = 0
        for i in range(0,n):
            for j in range (i+1,n):
                if prices[j]>prices[i]:
                    p = prices[j]-prices[i]
                    if p>max:
                        max = p
        return max





# optimal solution 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            current_profit = price - min_price

            if current_profit > profit:
                profit = current_profit

        return profit
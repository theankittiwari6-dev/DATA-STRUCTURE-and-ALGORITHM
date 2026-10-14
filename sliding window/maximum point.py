class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        maxi = 0
        r_sum = 0
        l_sum = 0
        for i in range(0,k):
            l_sum += cardPoints[i]
        maxi = l_sum
        r_ind = n-1
        for i in range(k-1,-1,-1):
            l_sum -= cardPoints[i]
            r_sum += cardPoints[r_ind]
            maxi = max(maxi , l_sum+r_sum)
            r_ind-=1
        return maxi                
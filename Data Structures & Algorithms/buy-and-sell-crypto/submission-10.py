class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProf = 0

        for r in range(len(prices)):
            currProfit = 0
            if prices[r] > prices[l]:
                currProfit = prices[r] - prices[l]
            elif prices[r] < prices[l]:
                l = r 
            maxProf = max(maxProf,currProfit)
        return maxProf 
class Solution:
    def maxProfit(self, prices):
        maxProf = 0
        minSoFar = float('infinity')
        l = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                if prices[l] <= minSoFar:
                    maxProf = max(maxProf,prices[r]-prices[l])
                    minSoFar = prices[l]
            if prices[r] < prices[l]:
                l = r
        return maxProf
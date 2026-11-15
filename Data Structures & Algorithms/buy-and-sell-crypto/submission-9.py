class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProf = 0
        for r in range(len(prices)):
            if l == r: 
                continue
            currProfit = 0 
            if prices[r] > prices[l]:
                currProfit = prices[r] - prices[l]
                maxProf = max(maxProf,currProfit)
            else:
                l = r 
        return maxProf
            
